# ---------------------------------------------------------------------------
# IntelligentDistribution_v2.pyt
#
# Description:
#   An ArcGIS Pro tool that takes clustered points and intelligently distributes
#   them based on population density. This version uses a robust "filter locally"
#   pattern for web service queries to ensure high precision.
# ---------------------------------------------------------------------------
# Author - Jhonatan Garrido-Lecca

import arcpy
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import os

class Toolbox:
    def __init__(self):
        """Define the toolbox."""
        self.label = "Intelligent Distribution Tools"
        self.alias = "intel_v2"
        self.tools = [DistributePointsByPopulation]

class DistributePointsByPopulation:
    def __init__(self):
        """Define the tool class."""
        self.label = "Distribute Points by Population (Precise Intersect)"
        self.description = "Takes points clustered at a single location and distributes them within an Area of Interest based on the population density of underlying census blocks."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define the tool's user interface (the parameters)."""
        
        param0 = arcpy.Parameter(displayName="Points to Distribute", name="in_points", datatype="GPFeatureLayer", parameterType="Required", direction="Input")
        param1 = arcpy.Parameter(displayName="Area of Interest (AOI)", name="in_aoi", datatype="GPFeatureLayer", parameterType="Required", direction="Input")
        param2 = arcpy.Parameter(displayName="Output Distributed Points", name="out_features", datatype="DEFeatureClass", parameterType="Required", direction="Output")
        param3 = arcpy.Parameter(displayName="Census Data Source", name="census_source_choice", datatype="GPString", parameterType="Required", direction="Input")
        param3.filter.type = "ValueList"
        param3.filter.list = ["Use Local Census Layer", "Use Web Service"]
        param3.value = "Use Local Census Layer"
        param4 = arcpy.Parameter(displayName="Local Census Layer (e.g., Block Groups)", name="in_local_census", datatype="GPFeatureLayer", parameterType="Optional", direction="Input")
        param5 = arcpy.Parameter(displayName="Census Web Service URL", name="in_web_census_url", datatype="GPString", parameterType="Optional", direction="Input")
        param5.value = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0"
        param6 = arcpy.Parameter(displayName="Population Field", name="population_field", datatype="GPString", parameterType="Required", direction="Input")
        param6.value = "P0010001"

        return [param0, param1, param2, param3, param4, param5, param6]

    def updateParameters(self, parameters):
        """Modify the Esri tool GUI based on parameter values."""
        if parameters[3].valueAsText == "Use Local Census Layer":
            parameters[4].enabled = True
            parameters[5].enabled = False
        elif parameters[3].valueAsText == "Use Web Service":
            parameters[4].enabled = False
            parameters[5].enabled = True
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        
        in_points_fc      = parameters[0].valueAsText
        in_aoi_fc         = parameters[1].valueAsText
        out_features_fc   = parameters[2].valueAsText
        census_choice     = parameters[3].valueAsText
        local_census_fc   = parameters[4].valueAsText
        web_census_url    = parameters[5].valueAsText
        population_field  = parameters[6].valueAsText

        workspace = os.path.dirname(out_features_fc)
        arcpy.env.workspace = workspace
        arcpy.env.overwriteOutput = True
        
        study_area_fc = os.path.join(workspace, "intermediate_precise_study_area")
        join_id_field = "TEMP_JOIN_ID_XYZ"

        try:
            messages.addMessage("--- Workflow Started ---")

            # --- Step 1: Create Local Census Study Area ---
            messages.addMessage("Step 1: Preparing the census study area.")
            
            if census_choice == "Use Local Census Layer":
                if not local_census_fc:
                    messages.addError("Error: A local census layer must be provided for this option.")
                    return
                messages.addMessage(f"Intersecting local census data with the AOI...")
                arcpy.analysis.Intersect([local_census_fc, in_aoi_fc], study_area_fc, "ALL")

            elif census_choice == "Use Web Service":
                # --- THIS IS THE NEW WORKFLOW ---
                # 1a. Query by extent
                messages.addMessage("Querying web service using the AOI's bounding box...")
                desc = arcpy.Describe(in_aoi_fc)
                arcpy_extent = desc.extent
                extent_dict = {"xmin": arcpy_extent.XMin, "ymin": arcpy_extent.YMin, "xmax": arcpy_extent.XMax, "ymax": arcpy_extent.YMax, "spatialReference": {"wkid": arcpy_extent.spatialReference.factoryCode}}
                
                gis = GIS("pro")
                web_layer = FeatureLayer(web_census_url)
                queried_featureset = web_layer.query(geometry_filter={'geometry': extent_dict, 'spatialRel': 'esriSpatialRelIntersects'})
                
                if len(queried_featureset.features) == 0:
                    messages.addError("The web query returned no features for the given extent. Tool cannot continue.")
                    return
                
                intermediate_web_results = os.path.join(workspace, "intermediate_web_results")
                queried_featureset.save(save_location=workspace, out_name=os.path.basename(intermediate_web_results))
                
                # 1b. Perform precise intersect locally
                messages.addMessage("Performing precise local intersection...")
                arcpy.analysis.Intersect([in_aoi_fc, intermediate_web_results], study_area_fc, "ALL", output_type="INPUT")
                
                # Clean up the intermediate extent-based layer
                arcpy.management.Delete(intermediate_web_results)
            
            messages.addMessage("Study area created successfully.")

            # --- Step 2: Count Features in the Point Layer ---
            messages.addMessage("Step 2: Counting records in the input point layer.")
            count_result = arcpy.management.GetCount(in_points_fc)
            point_count = int(count_result.getOutput(0))

            if point_count == 0:
                messages.addWarning("Input point layer has no features. The tool will stop.")
                return
            messages.addMessage(f"Found {point_count} records to distribute.")

            # --- Step 3: Create the Spatially Sampled Locations ---
            messages.addMessage("Step 3: Creating new, spatially distributed point locations.")
            arcpy.management.CreateSpatialSamplingLocations(
                in_study_area=study_area_fc,
                out_features=out_features_fc,
                sampling_method="STRAT_POLY",
                strata_count_method="PROP_FIELD",
                population_field=population_field,
                num_samples=point_count,
                geometry_type="POINT"
            )
            messages.addMessage("New locations created.")

            # --- Step 4: Transfer Attributes to New Points ---
            messages.addMessage("Step 4: Transferring attributes.")
            # Programmatically get the OID field name for both layers to support shapefiles and geodatabases
            oid_field_in = arcpy.Describe(in_points_fc).OIDFieldName
            oid_field_out = arcpy.Describe(out_features_fc).OIDFieldName
            
            arcpy.management.AddField(in_points_fc, join_id_field, "LONG")
            arcpy.management.AddField(out_features_fc, join_id_field, "LONG")
            arcpy.management.CalculateField(in_points_fc, join_id_field, f"!{oid_field_in}!", "PYTHON3")
            arcpy.management.CalculateField(out_features_fc, join_id_field, f"!{oid_field_out}!", "PYTHON3")
            
            fields_to_join = [f.name for f in arcpy.ListFields(in_points_fc) if not f.required and f.name != join_id_field]
            arcpy.management.JoinField(
                in_data=out_features_fc, in_field=join_id_field,
                join_table=in_points_fc, join_field=join_id_field,
                fields=fields_to_join
            )
            messages.addMessage("Attribute transfer complete.")

            # --- Step 5: Final Cleanup ---
            messages.addMessage("Step 5: Cleaning up intermediate data...")
            arcpy.management.DeleteField(out_features_fc, join_id_field)
            arcpy.management.DeleteField(in_points_fc, join_id_field)
            arcpy.management.Delete(study_area_fc)
            messages.addMessage("Cleanup complete.")
            messages.addMessage("\n--- WORKFLOW FINISHED ---")

        except arcpy.ExecuteError:
            messages.addError(arcpy.GetMessages(2))
        except Exception as e:
            messages.addError(f"A non-tool error occurred: {e}")
        
        return

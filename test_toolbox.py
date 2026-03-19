import sys
import types
from unittest.mock import MagicMock, patch

# Create mock objects for the required modules
mock_arcpy = MagicMock()
mock_arcgis = MagicMock()
mock_arcgis_gis = MagicMock()
mock_arcgis_features = MagicMock()

# Set up some basic behavior for the mocks to allow the script to pass through the execution path
mock_arcpy.Describe.return_value.extent.XMin = 0
mock_arcpy.Describe.return_value.extent.YMin = 0
mock_arcpy.Describe.return_value.extent.XMax = 10
mock_arcpy.Describe.return_value.extent.YMax = 10
mock_arcpy.Describe.return_value.extent.spatialReference.factoryCode = 4326
mock_arcpy.Describe.return_value.OIDFieldName = "OBJECTID"
mock_arcpy.management.GetCount.return_value.getOutput.return_value = "10"

# Mock the FeatureLayer and query method
mock_feature_layer_instance = MagicMock()
mock_featureset = MagicMock()
mock_featureset.features = [1, 2, 3] # Ensure len() > 0
mock_feature_layer_instance.query.return_value = mock_featureset
mock_arcgis_features.FeatureLayer.return_value = mock_feature_layer_instance

# Inject the mock modules into sys.modules
sys.modules['arcpy'] = mock_arcpy
sys.modules['arcgis'] = mock_arcgis
sys.modules['arcgis.gis'] = mock_arcgis_gis
sys.modules['arcgis.features'] = mock_arcgis_features

# Load the toolbox dynamically
with open('IntelligentDistribution_v2.pyt', 'r') as file:
    code = file.read()

# Create a module dynamically
toolbox_module = types.ModuleType('toolbox_module')
exec(code, toolbox_module.__dict__)

def test_web_service_path():
    print("Testing DistributePointsByPopulation with Web Service option...")

    # Instantiate the tool
    tool = toolbox_module.DistributePointsByPopulation()

    # Mock parameters based on the parameter definitions
    # param0: in_points
    # param1: in_aoi
    # param2: out_features
    # param3: census_source_choice
    # param4: in_local_census
    # param5: in_web_census_url
    # param6: population_field

    class MockParameter:
        def __init__(self, valueAsText):
            self.valueAsText = valueAsText

    parameters = [
        MockParameter("mock_in_points"),
        MockParameter("mock_in_aoi"),
        MockParameter("mock_out_features"),
        MockParameter("Use Web Service"),
        MockParameter(""),
        MockParameter("http://mock_url"),
        MockParameter("MOCK_POP_FIELD")
    ]

    mock_messages = MagicMock()

    # Execute the tool
    tool.execute(parameters, mock_messages)

    # Verify the query was called correctly
    mock_feature_layer_instance.query.assert_called_once()
    call_kwargs = mock_feature_layer_instance.query.call_args[1]

    print(f"Query called with kwargs: {call_kwargs}")
    assert call_kwargs.get('out_fields') == "MOCK_POP_FIELD", f"Expected out_fields to be 'MOCK_POP_FIELD', got {call_kwargs.get('out_fields')}"

    print("Test passed successfully!")

if __name__ == "__main__":
    test_web_service_path()

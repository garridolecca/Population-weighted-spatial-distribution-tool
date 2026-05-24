
## 2026-05-24 - Optimize arcgis FeatureLayer queries
**Learning:** When querying web services via arcgis.features.FeatureLayer, omitting the out_fields parameter causes the API to retrieve all fields, increasing network load and latency unnecessarily.
**Action:** Always explicitly specify out_fields (e.g., out_fields=population_field) when querying ArcGIS web services to limit data transfer to only the required attributes.

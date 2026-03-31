
## 2024-05-14 - [Limit out_fields for arcgis.features.FeatureLayer]
**Learning:** Limiting `out_fields` to only the required attributes when querying a web service via `arcgis.features.FeatureLayer` is a crucial pattern for reducing network payload size and latency in ArcGIS environments, especially since full census layers can be extremely wide.
**Action:** Always include the `out_fields` parameter when executing spatial queries against web feature services to optimize data retrieval and execution speed.

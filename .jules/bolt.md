## 2024-06-01 - [Limit web service query fields]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, fetching all fields by default can cause significant network load and latency, especially for large datasets like census blocks.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only the necessary attributes.
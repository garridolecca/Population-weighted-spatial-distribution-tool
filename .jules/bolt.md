## 2026-10-17 - ArcGIS FeatureLayer Query Payload Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census data, this results in large, inefficient network payloads.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `FeatureLayer`s to reduce data transfer and improve performance. Spatial geometry is safely returned by default.

## 2026-11-11 - ArcGIS FeatureLayer Query Optimization
**Learning:** The ArcGIS `FeatureLayer.query()` fetches all fields by default, which creates a huge network bottleneck for wide datasets like census data.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when performing spatial queries to reduce payload size and execution time.

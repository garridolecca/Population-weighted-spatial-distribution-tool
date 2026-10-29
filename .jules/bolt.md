## 2026-10-29 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payloads and performance bottlenecks for wide datasets like census data.
**Action:** Always specify the required fields using the `out_fields` parameter when using `FeatureLayer.query()` to reduce network payload and improve performance.

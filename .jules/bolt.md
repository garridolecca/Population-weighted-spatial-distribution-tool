## 2026-10-25 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data.
**Action:** Always specify the required fields using the `out_fields` parameter when querying ArcGIS web services to minimize payload size and improve performance.

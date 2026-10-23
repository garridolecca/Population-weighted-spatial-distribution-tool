## 2026-10-23 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload bottlenecks when querying wide datasets like census data.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when executing `query()` to minimize data transfer overhead, noting that geometry is still returned safely by default.

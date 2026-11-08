## 2026-11-08 - Optimize ArcGIS FeatureLayer Query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data.
**Action:** Always specify the required fields using the `out_fields` parameter to minimize data transfer and speed up queries.

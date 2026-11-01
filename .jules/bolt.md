## 2026-11-01 - Optimize ArcGIS FeatureLayer.query

**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead when querying wide datasets like census data.

**Action:** Always specify the required fields using the `out_fields` parameter to optimize performance and reduce memory usage.

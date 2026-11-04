## 2026-11-04 - Optimize ArcGIS FeatureLayer.query() network payloads
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets (like census data), this creates unnecessarily large network payloads.
**Action:** Always specify required fields using the `out_fields` parameter when querying feature layers to optimize network usage and improve performance.

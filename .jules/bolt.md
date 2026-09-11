## 2026-09-11 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census data, this results in massive network payloads and slow query performance.
**Action:** Always specify the required fields using the `out_fields` parameter to reduce network payload and improve performance.

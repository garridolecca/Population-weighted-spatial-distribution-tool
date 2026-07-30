## 2026-07-30 - Optimize ArcGIS FeatureLayer Query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census blocks, this causes significant network overhead when we only need specific fields (e.g., population data). Geometry is still returned by default even when `out_fields` is specified.
**Action:** Always specify the required fields using the `out_fields` parameter to reduce network payload and speed up queries.

## 2026-10-18 - Optimize ArcGIS FeatureLayer query with out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. This can cause massive network payloads for wide datasets like census blocks. `returnGeometry` defaults to `True`, so specifying `out_fields` still returns geometry safely.
**Action:** Always specify required fields using the `out_fields` parameter when querying `FeatureLayer` to optimize performance and reduce network payload.

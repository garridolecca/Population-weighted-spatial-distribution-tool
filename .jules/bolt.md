## 2026-10-12 - Optimize ArcGIS FeatureLayer Queries by Explicitly Requesting Fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload bloat and performance degradation, especially for wide datasets like census blocks. Specifying `out_fields` drastically reduces this payload while still returning geometry.
**Action:** Always specify the `out_fields` parameter when querying `FeatureLayer` objects if only specific attribute fields are needed.

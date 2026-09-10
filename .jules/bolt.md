## 2026-09-10 - Optimize FeatureLayer.query() Payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network bottlenecks for wide census datasets.
**Action:** Always specify the `out_fields` parameter when querying web features to reduce network payload. Geometry is returned by default, so it remains safe for spatial operations.

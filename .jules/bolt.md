## 2026-10-16 - Optimize FeatureLayer.query() Payload

**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant performance bottlenecks in network payload and memory when querying wide datasets like census blocks.

**Action:** Always specify the required fields using the `out_fields` parameter when using `FeatureLayer.query()`. Geometry will still be returned by default (`returnGeometry=True`) if needed for spatial operations.

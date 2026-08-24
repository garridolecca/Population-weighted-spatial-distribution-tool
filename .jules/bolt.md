## 2026-08-24 - Optimize ArcGIS FeatureLayer Query Payload
**Learning:** By default, `FeatureLayer.query()` fetches all fields (`out_fields='*'`). For wide datasets like census blocks, this causes massive network payload overhead. Using `out_fields` restricts the fetched attributes without losing the spatial geometry (as `returnGeometry` defaults to `True`).
**Action:** Always specify the exact required fields using `out_fields` when calling `FeatureLayer.query()` to optimize performance and reduce network latency.

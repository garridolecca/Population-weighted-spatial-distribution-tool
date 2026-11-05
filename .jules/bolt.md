## 2026-11-05 - Optimize ArcGIS FeatureLayer.query() Payload
**Learning:** By default, `FeatureLayer.query()` fetches all fields. For wide datasets like census data, this results in significant network payload.
**Action:** Always specify the required fields using the `out_fields` parameter when performing spatial queries to optimize performance and reduce memory usage.

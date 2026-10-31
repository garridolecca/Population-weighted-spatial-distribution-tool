## 2026-10-31 - Optimize FeatureLayer.query out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census blocks, this creates massive network payloads.
**Action:** Always specify the required fields using the `out_fields` parameter when using `FeatureLayer.query()` to reduce network load and memory usage.

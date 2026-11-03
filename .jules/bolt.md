## 2026-11-03 - Optimize FeatureLayer.query fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets (like census data), this causes large network payloads and memory usage.
**Action:** Always specify the required fields using the `out_fields` parameter when performing queries on FeatureLayers to optimize performance.

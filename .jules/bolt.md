## 2026-09-12 - Optimize FeatureLayer query to reduce network payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. This causes large network payloads for wide datasets (like census data).
**Action:** Always specify the required fields using the `out_fields` parameter to optimize performance and reduce network payload.

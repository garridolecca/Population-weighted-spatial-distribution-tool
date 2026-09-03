## 2026-09-03 - Optimize FeatureLayer query by requesting only required fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause large network payloads for wide datasets like census data.
**Action:** Use the `out_fields` parameter to explicitly request only the required fields.

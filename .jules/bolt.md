## 2026-08-29 - [Optimize FeatureLayer.query() with out_fields]
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, returning spatial geometry data along with it. This can lead to massive, inefficient network payloads for wide datasets (like census data).
**Action:** Always specify the required fields using the `out_fields` parameter when performing spatial queries to reduce the payload size.

## 2026-10-21 - Optimize FeatureLayer web query payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause massive network payloads for wide datasets like census data.
**Action:** Always specify the required fields using the `out_fields` parameter when performing web queries to improve performance and reduce network overhead.

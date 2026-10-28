## 2026-10-28 - Optimize web service query payload size by specifying out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census data, this results in unnecessarily large network payloads.
**Action:** Always specify the `out_fields` parameter in `FeatureLayer.query()` to retrieve only the fields required for the operation.

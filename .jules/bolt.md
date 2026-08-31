## 2026-08-31 - Optimize web service query payload by requesting only required fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, and specifying `out_fields` optimizes performance for wide datasets like census blocks without losing default geometry data.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `arcgis.features.FeatureLayer` to reduce network payload.

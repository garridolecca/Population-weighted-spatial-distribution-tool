## 2026-09-17 - Optimize FeatureLayer queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause large network payloads for wide datasets like census data. `returnGeometry` defaults to `True` so geometry is safely returned even if `out_fields` is specified.
**Action:** Always specify required fields using the `out_fields` parameter when querying FeatureLayers to reduce network payload.

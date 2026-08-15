## 2026-08-15 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network overhead and memory usage for wide datasets (like census data).
**Action:** Always specify the required fields using the `out_fields` parameter when querying FeatureLayers to reduce network payload. `returnGeometry` defaults to `True`, so geometry is safely returned without needing to be explicitly requested.

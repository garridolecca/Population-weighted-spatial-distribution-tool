## 2026-08-27 - Optimize FeatureLayer Query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. To optimize performance and reduce network payload for wide datasets (e.g., census data), always specify the required fields using the `out_fields` parameter. The geometry is still returned because `returnGeometry` defaults to True.
**Action:** Always use `out_fields` parameter when calling `FeatureLayer.query()` to fetch only required fields and improve performance.

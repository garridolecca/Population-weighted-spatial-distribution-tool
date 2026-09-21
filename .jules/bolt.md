## 2026-09-21 - Optimize arcgis FeatureLayer queries
**Learning:** In ArcGIS API for Python, `FeatureLayer.query()` fetches all fields by default, which can cause severe network payload bloat when querying wide datasets like Census blocks. However, `returnGeometry` defaults to True, so you can safely restrict attributes without losing spatial data.
**Action:** Always explicitly use the `out_fields` parameter when performing feature queries, specifying only the fields required for the operation.

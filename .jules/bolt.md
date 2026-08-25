## 2026-08-25 - Optimize FeatureLayer.query out_fields
**Learning:** ArcGIS `FeatureLayer.query()` returns all attributes by default, causing performance bottlenecks for wide datasets. `returnGeometry` defaults to `True`, so geometry is safely preserved when restricting fields.
**Action:** Always specify the `out_fields` parameter when querying FeatureLayers to fetch only required fields and reduce network payloads.

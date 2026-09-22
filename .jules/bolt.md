## Bolt Journal
## 2024-05-15 - Optimize FeatureLayer Web Service Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload bottlenecks for wide datasets like Census data. The `returnGeometry` defaults to `True`, so spatial joins remain intact even if we restrict fields.
**Action:** Always specify the exact required fields using the `out_fields` parameter when calling `FeatureLayer.query()` to minimize payload and speed up web service downloads.

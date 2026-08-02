## 2026-08-02 - [Optimize FeatureLayer Query]
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census data, this results in significant unnecessary network transfer.
**Action:** Always use the `out_fields` parameter to explicitly request only the required fields. `returnGeometry` defaults to True, so spatial geometry is safely preserved.

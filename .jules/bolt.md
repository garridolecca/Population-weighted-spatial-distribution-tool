## 2026-10-14 - Optimize Web Service Queries

**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload issues, especially for wide datasets like Census data. The `returnGeometry` parameter defaults to True, so spatial geometry data will still be returned even if not requested explicitly in `out_fields`.
**Action:** Always specify the required fields using the `out_fields` parameter in `FeatureLayer.query()` to minimize network payload when querying ArcGIS web services.

## 2026-10-20 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data. Geometry is still safely returned even if we restrict fields.
**Action:** Always specify the required fields using the `out_fields` parameter when querying FeatureLayers to minimize data transfer and improve performance.

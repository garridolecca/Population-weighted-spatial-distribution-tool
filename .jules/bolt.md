## 2026-10-13 - Optimize ArcGIS FeatureLayer Query Performance
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data. However, the `returnGeometry` parameter safely defaults to `True`, allowing optimization of attribute fetching while retaining required geometry.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `FeatureLayer` objects to reduce data transfer size and improve performance.

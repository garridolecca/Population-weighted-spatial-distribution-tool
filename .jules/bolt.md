## 2026-08-28 - Optimize ArcGIS FeatureLayer queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data.
**Action:** Always specify the required fields using the `out_fields` parameter. Remember that `returnGeometry` defaults to True, so spatial data is still safely returned.

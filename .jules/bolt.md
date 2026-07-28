## 2026-07-28 - Optimize FeatureLayer web query payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can create a large network payload for wide datasets like census data. Geometry is still returned by default, so we can use `out_fields` to restrict the attributes.
**Action:** Always specify required fields using `out_fields` to reduce network payload and improve query speed.

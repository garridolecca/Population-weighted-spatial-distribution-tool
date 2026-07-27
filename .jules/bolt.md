## 2026-07-27 - [Optimize FeatureLayer.query out_fields]
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, causing massive network payloads for wide datasets like census blocks.
**Action:** Always specify the required fields using the `out_fields` parameter to reduce network payload. `returnGeometry` defaults to `True`, so geometry is safely returned.

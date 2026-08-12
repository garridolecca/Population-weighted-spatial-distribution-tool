## 2026-08-12 - [FeatureLayer default fields overhead]
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, causing unnecessary network overhead for wide datasets like census data when only specific fields are needed.
**Action:** Always specify the required fields using the `out_fields` parameter to reduce payload, remembering that spatial geometry is safely returned since `returnGeometry` defaults to `True`.

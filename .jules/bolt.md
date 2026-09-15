## Bolt's Journal
## 2026-09-15 - Optimize FeatureLayer query by limiting output fields
**Learning:** By default, ArcGIS `FeatureLayer.query()` fetches all fields. For wide datasets like census blocks, this causes significant unnecessary network payload.
**Action:** Always specify the required fields using the `out_fields` parameter. Geometry data is still returned by default (`returnGeometry=True`), ensuring spatial operations remain unaffected while drastically reducing payload size.

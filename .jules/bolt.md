## 2026-08-05 - [Optimize ArcGIS FeatureLayer web queries]
**Learning:** `FeatureLayer.query()` fetches all fields by default (`out_fields='*'`). For wide datasets like census blocks, this creates a massive unnecessary network payload.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `FeatureLayer`, as `returnGeometry` safely defaults to True and geometry is still returned.

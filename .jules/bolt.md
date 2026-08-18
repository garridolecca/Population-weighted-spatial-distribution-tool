## 2026-08-18 - Optimize FeatureLayer.query() payload size
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census blocks, this results in massive, slow network payloads.
**Action:** Always specify the `out_fields` parameter with only the required fields (e.g., `out_fields=population_field`). Geometry is implicitly returned by default, preserving spatial operations without unnecessary attribute overhead.

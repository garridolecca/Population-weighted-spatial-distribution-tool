## 2026-07-31 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default (`out_fields='*'`). For datasets with many attributes (like census data), this causes massive unnecessary network payloads, even if we only need a single field. Geometry is still returned by default when `out_fields` is restricted.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when calling `FeatureLayer.query()` to reduce payload size and improve execution time.

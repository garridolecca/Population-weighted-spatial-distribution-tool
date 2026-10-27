## 2026-10-27 - Restrict ArcGIS FeatureLayer Query Fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census blocks, this causes huge unnecessary network payloads when only a specific field (like population) and geometry are needed.
**Action:** Always specify the `out_fields` parameter in ArcGIS queries to explicitly list required fields and minimize data transfer, significantly speeding up query time and reducing memory overhead.

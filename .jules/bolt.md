## 2026-09-08 - Optimize ArcGIS FeatureLayer queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause massive network payloads when querying wide datasets like census blocks.
**Action:** Always specify the required fields using the `out_fields` parameter when querying feature layers to minimize data transfer.

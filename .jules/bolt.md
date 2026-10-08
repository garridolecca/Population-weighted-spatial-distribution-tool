## 2026-10-08 - Optimize ArcGIS FeatureLayer query with out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can lead to unnecessarily large network payloads, especially for wide datasets like census blocks.
**Action:** Always restrict fetched fields using the `out_fields` parameter in `query()` to minimize payload size and memory usage.

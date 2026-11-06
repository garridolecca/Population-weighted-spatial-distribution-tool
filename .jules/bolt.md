## 2026-11-06 - ArcGIS FeatureLayer Query Performance
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like Census blocks, this results in massive network payloads.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when querying wide feature layers to optimize performance.

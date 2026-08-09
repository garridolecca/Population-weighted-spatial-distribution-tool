## 2026-08-09 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default (out_fields='*'). When querying wide datasets like Census data via web services, this results in massive, unnecessary network payloads since geometry is implicitly returned even when specifying fields.
**Action:** Always specify the exact fields needed using the `out_fields` parameter in `FeatureLayer.query()` to reduce network latency and memory overhead.

## 2026-06-04 - [Optimize FeatureLayer.query() payload]
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, causing massive payloads.
**Action:** Always specify `out_fields` to significantly reduce web service latency and payload size.

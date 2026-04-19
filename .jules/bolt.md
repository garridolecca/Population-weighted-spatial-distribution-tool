## 2026-04-19 - [FeatureLayer Network Payload Optimization]
**Learning:** Querying ArcGIS FeatureLayer services without explicitly specifying `out_fields` results in downloading all fields, significantly increasing network payload and decreasing performance.
**Action:** Always specify the minimum necessary attributes using the `out_fields` parameter when performing spatial queries against web services.

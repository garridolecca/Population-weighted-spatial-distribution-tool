## 2026-05-25 - [Optimize FeatureLayer Web Queries]
**Learning:** Querying web services without limiting retrieved fields leads to massive unnecessary data payloads.
**Action:** Always use the `out_fields` parameter on `FeatureLayer.query()` calls to retrieve only the required fields, reducing network load and latency.

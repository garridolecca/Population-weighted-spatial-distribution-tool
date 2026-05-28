## 2026-05-28 - Optimize Web Query Payload
**Learning:** Querying web services without specifying out_fields downloads all attributes, causing unnecessary network overhead and latency.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes when using FeatureLayer.query().

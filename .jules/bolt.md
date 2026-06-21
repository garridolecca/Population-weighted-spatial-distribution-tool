## 2026-06-21 - [FeatureLayer Web Service Queries]
**Learning:** Querying web services via arcgis.features.FeatureLayer without specifying `out_fields` pulls all fields, causing significant network overhead, especially with large datasets like census blocks.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

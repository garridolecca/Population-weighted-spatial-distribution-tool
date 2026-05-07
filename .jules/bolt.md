## 2026-05-07 - [FeatureLayer query optimization]
**Learning:** Querying web services via `arcgis.features.FeatureLayer` without specifying `out_fields` downloads all attributes, causing unnecessary network overhead.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

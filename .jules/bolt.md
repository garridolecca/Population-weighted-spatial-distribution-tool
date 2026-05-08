## 2026-05-08 - [Optimize FeatureLayer query network payload]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, omitting `out_fields` results in fetching all attributes, causing unnecessary network payload and latency.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load.

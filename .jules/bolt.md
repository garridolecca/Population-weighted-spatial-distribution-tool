## 2026-05-29 - [FeatureLayer query performance]
**Learning:** When querying web services via arcgis.features.FeatureLayer, querying without out_fields retrieves all attributes, which can cause significant network load and latency.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes to improve performance.

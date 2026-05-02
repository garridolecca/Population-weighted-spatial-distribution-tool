## 2026-05-02 - [Optimize FeatureLayer Query]
**Learning:** When querying web services via arcgis.features.FeatureLayer, always use the out_fields parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Pass `out_fields=[required_field]` or similar to limit returned attributes.

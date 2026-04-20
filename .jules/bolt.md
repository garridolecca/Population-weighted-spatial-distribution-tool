## 2026-04-20 - [Optimize FeatureLayer Query]
**Learning:** When querying web services via arcgis.features.FeatureLayer, requesting all fields by default causes unnecessary network overhead and memory usage, particularly when only specific fields are needed.
**Action:** Always use the out_fields parameter in FeatureLayer.query() to limit data retrieval to only necessary attributes, reducing network load and latency.

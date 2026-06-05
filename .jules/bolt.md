## 2026-06-05 - [Limit web service query fields]
**Learning:** When querying web services via arcgis.features.FeatureLayer, always use the out_fields parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Always include out_fields when making queries to feature layers if not all fields are needed.

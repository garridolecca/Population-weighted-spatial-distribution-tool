## 2026-04-18 - [Optimize Web Service Queries]
**Learning:** When querying web services via arcgis.features.FeatureLayer, always use the out_fields parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Always include out_fields parameter with only required fields when using web_layer.query()

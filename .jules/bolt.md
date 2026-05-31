## 2026-05-31 - [Network payload optimization]
**Learning:** When querying web services via arcgis.features.FeatureLayer, omitting the out_fields parameter causes all attributes to be downloaded. This is inefficient. We can explicitly specify the out_fields parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Always use the out_fields parameter when querying FeatureLayer to limit data retrieval.

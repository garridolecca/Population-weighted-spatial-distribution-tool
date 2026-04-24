## 2026-04-24 - Optimize FeatureLayer query using out_fields
**Learning:** When querying web services via arcgis.features.FeatureLayer, the default behavior is to retrieve all fields.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

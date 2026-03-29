## 2024-05-18 - [Limit ArcGIS Web Query Payloads]
**Learning:** When querying web services via `arcgis.features.FeatureLayer` (e.g. `web_layer.query()`), the query can pull back large amounts of attribute data unnecessarily, increasing network latency and payload size.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, effectively reducing network load and latency. For example: `out_fields=population_field`.

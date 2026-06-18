## 2026-06-18 - [Reduce Web Service Query Payload]
**Learning:** When querying web services via `arcgis.features.FeatureLayer.query()`, it downloads all fields by default, which can cause significant network payload and latency.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes (e.g., the population field) when making web service queries.

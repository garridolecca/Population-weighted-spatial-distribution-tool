## 2026-05-12 - [Optimize Web Service Queries]
**Learning:** ArcGIS feature layers can return excessive payloads if not restricted.
**Action:** Always use the `out_fields` parameter when querying web services via `arcgis.features.FeatureLayer` to limit data retrieval to only necessary attributes, reducing network load and latency.

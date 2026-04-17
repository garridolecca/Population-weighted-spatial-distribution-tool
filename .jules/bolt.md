## 2026-04-17 - Optimize FeatureLayer.query network payload
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Pass `out_fields=population_field` in `web_layer.query()` instead of pulling all fields.

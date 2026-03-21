## 2024-03-05 - [Web Service Query Optimization]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, requesting the full payload (all fields) is a significant performance bottleneck and increases network load/latency.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only the necessary attributes.

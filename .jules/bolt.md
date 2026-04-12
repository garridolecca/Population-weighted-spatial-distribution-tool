## 2026-04-12 - [Optimize FeatureLayer Web Queries]
**Learning:** By default, arcgis.features.FeatureLayer queries fetch all fields, which can lead to large payloads and high latency when querying external web services.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only necessary attributes, significantly reducing network load.

## 2024-05-18 - [Optimize Web Service Query]
**Learning:** When querying web services via `arcgis.features.FeatureLayer` in ArcGIS tool development, fetching all fields by default can significantly impact network load and latency, especially when only a specific attribute (like a population field) is needed.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes when using `web_layer.query()`.

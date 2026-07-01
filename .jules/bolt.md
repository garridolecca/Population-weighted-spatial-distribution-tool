## 2026-07-01 - Optimize arcgis FeatureLayer queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. This can cause large, unnecessary network payloads, especially with dense datasets like census data. However, the `returnGeometry` parameter defaults to `True`, meaning spatial geometry data is still returned even when limiting attributes.
**Action:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

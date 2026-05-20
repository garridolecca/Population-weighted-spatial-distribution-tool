## 2026-05-20 - ArcGIS FeatureLayer Query Optimization
**Learning:** Querying web services via `arcgis.features.FeatureLayer` without specifying fields retrieves all attributes, which can be hundreds of columns for census data, causing severe network overhead.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only necessary attributes (like the population field), reducing network payload and latency.

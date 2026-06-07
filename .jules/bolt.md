## 2026-06-07 - [FeatureLayer query Optimization]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer.query()`, pulling all fields is a major performance bottleneck, especially for census data which can contain hundreds of attributes.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes to significantly reduce network load and latency.

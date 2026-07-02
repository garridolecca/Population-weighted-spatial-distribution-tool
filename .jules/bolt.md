## 2026-07-02 - [Optimize FeatureLayer Web Queries]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, omitting `out_fields` results in downloading all fields (which for census data can be massive). `returnGeometry` defaults to `True`, so spatial data is still preserved.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only necessary attributes, minimizing network load and latency.

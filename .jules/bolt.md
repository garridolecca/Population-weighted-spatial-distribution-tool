
## 2026-06-24 - [FeatureLayer query performance anti-pattern]
**Learning:** Querying `arcgis.features.FeatureLayer` over web services without specifying `out_fields` defaults to returning all attributes, causing significant network bloat and latency, especially with dense census layers.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes (e.g., `out_fields=population_field`). Note that `returnGeometry` defaults to `True`, so spatial data is preserved automatically.

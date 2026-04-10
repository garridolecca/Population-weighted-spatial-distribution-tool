## 2026-04-10 - [FeatureLayer query performance optimization]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, downloading all fields (the default behavior) causes massive memory and network overhead, especially for dense spatial datasets like Census blocks.
**Action:** Always use the `out_fields` parameter in `web_layer.query()` to limit data retrieval to only necessary attributes.

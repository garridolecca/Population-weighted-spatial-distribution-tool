## 2026-04-09 - [FeatureLayer query performance]
**Learning:** Querying web services without restricting fields pulls down all attribute data, which increases network latency.
**Action:** Always use the `out_fields` parameter in `arcgis.features.FeatureLayer.query` to limit data retrieval.

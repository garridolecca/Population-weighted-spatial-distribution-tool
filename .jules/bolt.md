## 2026-04-02 - [Optimize arcgis.features.FeatureLayer web query]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, not specifying `out_fields` can fetch unnecessary columns, significantly increasing network payload and latency.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only the necessary attributes.

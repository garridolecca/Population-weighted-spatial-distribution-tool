## 2026-04-30 - [FeatureLayer query optimization]
**Learning:** When querying web services via arcgis.features.FeatureLayer, fetching all fields by default can lead to unnecessary network load and latency.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes.

## 2026-05-23 - [FeatureLayer query performance]
**Learning:** When querying web services via arcgis.features.FeatureLayer, requesting all fields by default creates unnecessary network payload and latency.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes (like population).

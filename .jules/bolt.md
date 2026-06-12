## 2026-06-12 - Limit returned fields on web service queries
**Learning:** When querying web services via arcgis.features.FeatureLayer, fetching all fields by default can introduce unnecessary network load and processing latency.
**Action:** Always use the out_fields parameter to limit data retrieval to only necessary attributes when querying web services.

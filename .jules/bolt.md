## 2026-06-17 - Optimize Web Feature Queries via out_fields
**Learning:** Querying web services via arcgis.features.FeatureLayer without specifying out_fields retrieves all attributes, which can cause severe network latency and payload bloat.
**Action:** Always use the out_fields parameter when making web feature queries to limit data retrieval to only the necessary fields.

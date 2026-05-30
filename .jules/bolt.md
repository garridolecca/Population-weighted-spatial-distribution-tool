## 2026-05-30 - [FeatureLayer Web Query Optimization]
**Learning:** Querying web services via arcgis.features.FeatureLayer without specifying out_fields retrieves all fields by default, causing unnecessary network load and latency, especially for large census datasets.
**Action:** Always use the out_fields parameter in FeatureLayer.query() to limit data retrieval to only necessary attributes (e.g., population_field).

## 2026-05-15 - Optimize FeatureLayer Web Query with out_fields
**Learning:** Found that querying web services via `arcgis.features.FeatureLayer` retrieves all fields by default, causing unnecessary network payload and latency when only a specific field is needed.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes when querying web services.

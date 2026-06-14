## 2026-06-14 - [ArcGIS FeatureLayer Query Optimization]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, omitting `out_fields` results in downloading all available attributes, which causes unnecessary network load and latency.
**Action:** Always use the `out_fields` parameter to explicitly limit data retrieval to only the fields required for the operation (e.g., `out_fields=population_field`).

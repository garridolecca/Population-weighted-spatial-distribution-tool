## 2026-06-09 - [FeatureLayer Queries Network Latency]
**Learning:** Fetching all fields from web census layers using `FeatureLayer.query` without specifying fields causes unnecessary network payload and latency.
**Action:** Whenever using `arcgis.features.FeatureLayer.query`, explicitly set the `out_fields` parameter to only retrieve required fields (e.g., `population_field`).

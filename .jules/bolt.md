## 2026-06-03 - [Optimize FeatureLayer Web Query]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, which significantly reduces network payload and latency.
**Action:** Ensure `out_fields` is specified whenever retrieving data from web layers, particularly when only a single field (e.g., population) is required.

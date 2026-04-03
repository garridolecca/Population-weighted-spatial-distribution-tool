## 2026-04-03 - [FeatureLayer out_fields Optimization]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, retrieving all fields by default creates unnecessary network overhead.
**Action:** Always use the `out_fields` parameter to restrict data retrieval to only the fields necessary for the tool's operation, reducing network payload and latency.

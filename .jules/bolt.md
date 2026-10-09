## 2026-10-09 - Optimize arcgis FeatureLayer.query Payload
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. This can drastically increase network payloads and execution time for wide datasets like census blocks.
**Action:** Always specify the required fields using the `out_fields` parameter (e.g., `out_fields=population_field`) to optimize performance and reduce network payload.

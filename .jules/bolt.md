## 2026-05-26 - [FeatureLayer query performance optimization]
**Learning:** By default, `arcgis.features.FeatureLayer.query()` retrieves all fields from the web service, which leads to bloated network payloads and slow execution times for dense census blocks.
**Action:** Always use the `out_fields` parameter to strictly limit data retrieval to only necessary attributes (e.g., `population_field`) when querying ArcGIS REST services.

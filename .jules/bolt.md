## 2024-05-18 - [Limit ArcGIS Web Service Retrievals]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, retrieving all fields over the network causes unnecessary latency, especially for large datasets.
**Action:** Always use the `out_fields` parameter to restrict data retrieval to only the necessary attributes (e.g., `out_fields=[population_field]`).

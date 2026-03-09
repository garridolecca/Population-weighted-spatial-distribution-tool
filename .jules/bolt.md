## 2024-05-24 - [Optimize ArcGIS Web Service Queries]
**Learning:** By default, querying web services via `arcgis.features.FeatureLayer` retrieves all fields, which can lead to large network payloads and increased latency. Using the `out_fields` parameter to request only necessary attributes is a critical codebase-specific performance pattern.
**Action:** Always use `out_fields` to limit data retrieval when querying ArcGIS web services.

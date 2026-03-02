## 2024-05-28 - Optimize ArcGIS REST API Queries
**Learning:** Querying web services without specifying `out_fields` retrieves all fields, leading to significant payload bloat and network latency.
**Action:** Always use the `out_fields` parameter in `arcgis.features.FeatureLayer.query()` to limit data retrieval to only necessary attributes.

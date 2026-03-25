## 2024-05-24 - [Optimize ArcGIS Feature Service Queries]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, requesting all fields by default can cause significant network payload and latency issues, especially with large datasets.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only the necessary attributes.

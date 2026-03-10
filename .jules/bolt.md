## 2024-05-24 - [Optimize ArcGIS FeatureLayer Queries]
**Learning:** `arcgis.features.FeatureLayer` queries retrieve all fields by default, which can cause significant network latency and payload bloat.
**Action:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

## 2026-05-05 - [Limit web service payload]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, the default behavior is to retrieve all fields, which can cause significant network load and latency.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes when querying web services.

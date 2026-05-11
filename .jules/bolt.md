## 2026-05-11 - [Limit Web Queries with out_fields]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, requesting all fields by default can cause significant network overhead and latency, especially for census layers with many demographic attributes.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only the necessary fields, reducing network payload.

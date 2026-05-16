## 2026-05-16 - Optimize Web Service Queries

**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, requesting all fields by default can lead to significant network overhead and latency, especially for large datasets or complex geometries.
**Action:** Always use the `out_fields` parameter in `query()` methods to limit data retrieval to only the necessary attributes.

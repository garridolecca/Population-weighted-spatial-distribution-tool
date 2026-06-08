# Bolt's Journal

## 2026-06-08 - Web Service Query Optimization
**Learning:** By default, `FeatureLayer.query()` retrieves all fields from a web service, which can significantly bloat network payloads and increase latency.
**Action:** Always use the `out_fields` parameter when querying ArcGIS web services to limit data retrieval to only the necessary attributes.

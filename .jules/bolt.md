## 2026-06-15 - [Limit Web Query to Required Fields]
**Learning:** In ArcGIS tool development, querying web services (`FeatureLayer`) without specifying `out_fields` can retrieve all attributes, leading to large payloads and increased network latency.
**Action:** Always use the `out_fields` parameter in `query()` to limit data retrieval to only necessary attributes (e.g., the population field) when fetching data from web services.

## 2026-06-20 - [Optimize FeatureLayer Web Query]
**Learning:** In the ArcGIS Python API, querying a `FeatureLayer` without specifying `out_fields` retrieves all fields. This is inefficient when only specific fields are needed, especially over a web service.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

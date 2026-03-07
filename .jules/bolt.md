## 2024-05-24 - [Optimize ArcGIS Web Service Queries with `out_fields`]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, the default behavior is to download all fields (the entire schema). For wide datasets like census blocks, this causes massive network payloads and severe latency, even if only one or two fields are needed for analysis.
**Action:** Always use the `out_fields` parameter in the `query()` method to limit data retrieval to only necessary attributes (e.g., `out_fields=["P0010001"]`), drastically reducing network load.

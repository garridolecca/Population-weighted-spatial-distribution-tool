## 2024-03-19 - [Optimize web service query with out_fields]
**Learning:** When using `arcgis.features.FeatureLayer` to query web services, the default behavior retrieves all attributes, resulting in significant network load and latency. Using the `out_fields` parameter directly limits data retrieval to only necessary attributes, which dramatically improves performance, especially when saving intermediate files.
**Action:** Always include the `out_fields` parameter when querying web services via `arcgis.features.FeatureLayer` if only a subset of fields is required for subsequent operations.

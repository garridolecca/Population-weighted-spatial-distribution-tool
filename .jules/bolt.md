
## 2024-05-18 - [Web Query Optimization]
**Learning:** ArcGIS FeatureLayer `query()` fetches all fields by default, causing massive network payload latency, especially for wide datasets like census block groups with hundreds of columns.
**Action:** When querying `arcgis.features.FeatureLayer`, ALWAYS use the `out_fields` argument to limit data retrieval to only the necessary fields (e.g., `out_fields=population_field`). This drastically reduces the response size and speeds up the geoprocessing tool.

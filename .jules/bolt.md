## 2026-04-05 - [Optimize FeatureLayer Query by Limiting Payload]
**Learning:** When querying web services using `arcgis.features.FeatureLayer`, retrieving all fields by default can result in significant network payloads and increased latency, especially for layers with many attributes like census data.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only the necessary fields (e.g., the population field) to optimize performance.

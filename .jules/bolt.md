## 2026-06-02 - [FeatureLayer Queries Optimization]
**Learning:** Querying web services via `arcgis.features.FeatureLayer` without specifying `out_fields` retrieves all attributes (which can be hundreds of demographic fields for Census data), severely impacting network performance and memory.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

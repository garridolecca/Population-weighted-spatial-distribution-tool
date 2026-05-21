## 2026-05-21 - [FeatureLayer Web Service Queries]
**Learning:** Querying web services using `arcgis.features.FeatureLayer` without specifying `out_fields` retrieves all attributes, which increases network load, memory consumption, and latency unnecessarily, especially for large datasets.
**Action:** Always use the `out_fields` parameter in `query()` to limit data retrieval to only the necessary attributes.

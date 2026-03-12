## 2024-05-28 - [Performance] Use out_fields parameter when querying arcgis.features.FeatureLayer
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, it is critical to use the `out_fields` parameter to limit data retrieval to only necessary attributes. Without it, all attributes are retrieved, unnecessarily increasing network payload size and latency.
**Action:** Always include the `out_fields` parameter to request only the required fields (e.g., `population_field`) when calling the `query` method on an `arcgis.features.FeatureLayer` object.

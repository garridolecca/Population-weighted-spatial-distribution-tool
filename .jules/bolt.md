## 2026-04-26 - [FeatureLayer Web Service Query Optimization]
**Learning:** The application queries ArcGIS REST services using `arcgis.features.FeatureLayer` but previously downloaded all feature attributes. By leveraging the `out_fields` parameter, we can restrict the requested fields to only those necessary (e.g., the population field), significantly reducing the payload size, network load, and latency.
**Action:** Always utilize the `out_fields` parameter in `FeatureLayer.query()` to minimize data retrieval to the required attributes.

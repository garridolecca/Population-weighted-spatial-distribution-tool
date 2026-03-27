## 2024-05-24 - [ArcGIS Feature Service Query Optimization]
**Learning:** By default, querying an ArcGIS Feature Service without specifying `out_fields` retrieves all fields for the intersected features, which can lead to significant network latency and memory overhead when only a specific field (like a population count) is needed.
**Action:** Always explicitly specify the `out_fields` parameter when calling `FeatureLayer.query()` to limit the data payload to only the required attributes.

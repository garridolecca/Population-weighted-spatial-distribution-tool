## 2024-05-24 - FeatureLayer Query Network Payload Bottleneck
**Learning:** By default, ArcGIS `FeatureLayer.query()` fetches all fields. For wide datasets like census data, this results in massive, unnecessary network payloads and severe performance degradation when only a single field (like population) is actually needed for spatial sampling.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when querying FeatureLayers to minimize network transfer. `returnGeometry` defaults to `True`, so spatial data is preserved without explicit request.

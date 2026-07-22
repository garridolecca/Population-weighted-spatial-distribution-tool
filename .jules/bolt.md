## 2026-07-22 - Optimize FeatureLayer.query payload
**Learning:** The `arcgis.features.FeatureLayer.query()` method retrieves all attributes by default, creating large payloads. Specifying `out_fields` restricts the payload size, and importantly, spatial geometries are still returned correctly as `returnGeometry` defaults to True.
**Action:** Always restrict queried fields when calling web service queries, especially for spatial intersections where only a single attribute (like population) is needed.

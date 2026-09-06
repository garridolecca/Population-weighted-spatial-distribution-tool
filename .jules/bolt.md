## 2026-09-06 - Optimize ArcGIS FeatureLayer web query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, creating a huge network payload when downloading wide census datasets. We only need the population field for the precise intersect later, and spatial geometries are returned automatically because `returnGeometry` defaults to `True`.
**Action:** Always add `out_fields` to `FeatureLayer.query()` to restrict network payloads, especially on wide feature services like USA Census blocks.

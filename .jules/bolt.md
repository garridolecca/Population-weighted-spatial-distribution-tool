## 2026-09-28 - Optimize ArcGIS FeatureLayer.query()
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which causes significant performance bottlenecks for wide datasets (like census data).
**Action:** Always specify required fields using the `out_fields` parameter when performing a `FeatureLayer.query()` to reduce network payload and memory overhead. Geometry data is still safely returned due to the default `returnGeometry=True`.

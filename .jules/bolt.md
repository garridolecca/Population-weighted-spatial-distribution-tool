## 2026-08-11 - Optimize ArcGIS FeatureLayer web queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. For wide datasets like census data, this results in significant unnecessary network payload and memory usage. The spatial geometry is still safely included when restricting fields, as `returnGeometry` defaults to `True`.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `FeatureLayer` objects to reduce payload size and improve performance.

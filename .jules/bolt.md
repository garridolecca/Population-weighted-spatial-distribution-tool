## 2026-09-01 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census data.
**Action:** Always specify required fields using the `out_fields` parameter (e.g., `out_fields=population_field`). Geometry is safely returned by default (`returnGeometry=True`).

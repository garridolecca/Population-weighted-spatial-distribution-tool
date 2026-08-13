## 2026-08-13 - Optimize ArcGIS FeatureLayer queries
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which can cause significant network payload bottlenecks for wide datasets like Census data.
**Action:** Always specify the `out_fields` parameter when performing spatial queries to reduce data transfer. Geometry is still returned by default (`returnGeometry=True`), so specifying `out_fields` won't break spatial intersections.

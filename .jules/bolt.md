## 2026-09-29 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network and memory bottlenecks when querying wide datasets like Census data.
**Action:** Always specify the `out_fields` parameter to explicitly fetch only the required fields (like the population field), as spatial geometry data is still returned safely by default (`returnGeometry=True`).

## 2026-10-22 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like Census data. Geometry is safely returned even when explicitly requesting specific fields.
**Action:** Always specify required fields using `out_fields` to optimize network performance.

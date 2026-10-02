## 2026-10-02 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead when querying wide datasets like census data. Geometry is returned by default, so explicit fields don't lose necessary spatial data.
**Action:** Always specify the required fields using the `out_fields` parameter when performing network queries via `FeatureLayer.query()` to minimize payload size and improve execution speed.

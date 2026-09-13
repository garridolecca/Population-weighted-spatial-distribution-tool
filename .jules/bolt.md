## 2024-05-18 - ArcGIS FeatureLayer Query Overhead
**Learning:** In the ArcGIS Python API, `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead when querying wide datasets like census blocks over web services.
**Action:** Always specify the `out_fields` parameter when calling `query()` on a `FeatureLayer` if only specific fields (and geometry) are required.

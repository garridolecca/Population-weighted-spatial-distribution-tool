## 2026-10-24 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which creates a significant network payload bottleneck when working with wide datasets (like census data).
**Action:** Always specify the `out_fields` parameter when querying feature layers to restrict the payload to only the explicitly required fields. The spatial geometry is still safely returned due to `returnGeometry` defaulting to True.

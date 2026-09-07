## 2026-09-07 - Optimize ArcGIS FeatureLayer query with out_fields
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default. For wide datasets like census blocks, this causes significant network overhead. Specifying `out_fields` reduces network payload size, and geometry is still safely returned because `returnGeometry` defaults to True.
**Action:** Always specify the required fields using the `out_fields` parameter when querying FeatureLayers to optimize performance.

## 2026-09-09 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS `FeatureLayer.query()` defaults to fetching all fields. For wide datasets like Census data, this causes unnecessary network overhead. The `returnGeometry` parameter defaults to True, so we can safely specify `out_fields` to fetch only the required attributes without losing spatial data.
**Action:** Always specify the minimum required fields using the `out_fields` parameter when querying ArcGIS FeatureLayers to minimize payload size.

## 2026-08-20 - Optimize ArcGIS FeatureLayer web queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets (like census data), this can cause significant network payload overhead. The `returnGeometry` parameter defaults to `True`, so geometry is safely returned even if only specific attribute fields are requested.
**Action:** Always specify the required fields using the `out_fields` parameter when querying FeatureLayers to reduce network payload, e.g., `out_fields=population_field`.

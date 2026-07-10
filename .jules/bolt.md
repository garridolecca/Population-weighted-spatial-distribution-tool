## 2026-07-10 - Optimize ArcGIS FeatureLayer web service query payload
**Learning:** The default behavior of `FeatureLayer.query()` in the arcgis package without `out_fields` fetches all attributes for features, creating an unnecessary large payload when only specific fields (like population) are needed.
**Action:** Always use the `out_fields` parameter to request only the required fields. When geometry is needed, it is returned by default (`returnGeometry` is True).

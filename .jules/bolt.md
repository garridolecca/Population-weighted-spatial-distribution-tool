## 2026-06-29 - [FeatureLayer query performance]
**Learning:** By default, arcgis.features.FeatureLayer queries return all fields from the web service, which can cause significant network latency for large datasets.
**Action:** Always use the `out_fields` parameter in web layer queries to request only the required fields (e.g., the population field). Geometry is returned by default.

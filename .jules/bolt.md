## 2026-09-25 - Optimize ArcGIS FeatureLayer query
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. For wide datasets like Census data, this can result in large network payloads.
**Action:** Always specify the required fields using the `out_fields` parameter in `query()` to reduce network I/O and speed up data retrieval.

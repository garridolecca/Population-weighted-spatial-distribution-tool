## 2026-09-05 - Optimize ArcGIS FeatureLayer query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, returning large JSON payloads for wide datasets like Census data. We only need the specific population field for the sampling logic (along with geometry which is returned by default).
**Action:** Always specify the `out_fields` parameter when calling `FeatureLayer.query()` to minimize payload size and improve execution time.

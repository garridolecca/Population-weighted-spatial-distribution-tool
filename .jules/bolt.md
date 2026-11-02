## 2026-11-02 - Optimize ArcGIS feature layer query by fetching only required fields
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which can be a significant performance bottleneck when querying wide datasets like census data over a web service.
**Action:** Always specify the `out_fields` parameter when using FeatureLayer.query() to fetch only the fields required for the subsequent processing steps, reducing network payload and memory usage.

## 2026-10-11 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which can cause significant network payload overhead when querying wide datasets like census data.
**Action:** Always specify the required fields using the out_fields parameter to minimize payload size.

## 2026-10-30 - Optimize ArcGIS FeatureLayer Query Network Payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause severe performance bottlenecks when querying wide datasets like census data over a network.
**Action:** Always specify the required fields using the `out_fields` parameter to minimize network payload size and reduce query latency.

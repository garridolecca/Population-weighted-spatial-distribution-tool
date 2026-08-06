## 2026-08-06 - [ArcGIS Query Optimization]
**Learning:** By default, ArcGIS `FeatureLayer.query()` fetches all fields. For wide datasets like census data, fetching unnecessary fields increases memory usage and network payload.
**Action:** Always specify the required fields using the `out_fields` parameter when querying ArcGIS web services to reduce data transfer size.

## 2026-08-16 - Optimize ArcGIS FeatureLayer Web Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant performance bottlenecks and large network payloads for wide datasets like Census data. Additionally, spatial geometry is safely returned by default (returnGeometry=True) even when explicitly requesting fields.
**Action:** Always use the `out_fields` parameter to explicitly request only the required fields when querying ArcGIS web services to reduce payload size and improve execution speed.

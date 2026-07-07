## 2026-07-07 - Optimize ArcGIS FeatureLayer Web Queries
**Learning:** By default, `arcgis.features.FeatureLayer.query` fetches all fields (`out_fields='*'`). When querying rich datasets like census blocks over a network, this causes massive, unnecessary data transfer. Since `returnGeometry` defaults to `True`, we can safely restrict `out_fields` to only the specific attributes needed for analysis (like the population field) without losing spatial data.
**Action:** Always explicitly set the `out_fields` parameter when querying web services to minimize payload size and improve network latency.

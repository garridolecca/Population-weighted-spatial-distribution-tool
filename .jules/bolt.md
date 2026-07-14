## 2026-07-14 - Optimize FeatureLayer query payload size
**Learning:** By default, ArcGIS FeatureLayer queries retrieve all available fields when fetching records. We only need the population field, and since `returnGeometry` defaults to `True` (meaning spatial geometry data will safely be returned), we can explicitly restrict `out_fields` to drastically reduce the network payload and memory footprint without losing necessary data.
**Action:** Always check what data is actually required and use the `out_fields` parameter to request exactly that, reducing query overhead.

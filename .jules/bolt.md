## 2026-08-07 - Optimize ArcGIS FeatureLayer Queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields for every feature, which causes significant network overhead and memory usage for wide datasets (like Census data). `returnGeometry` defaults to `True`, so geometry is safely returned even if fields are restricted.
**Action:** Always specify the required attributes using the `out_fields` parameter to minimize payload size when querying web layers.

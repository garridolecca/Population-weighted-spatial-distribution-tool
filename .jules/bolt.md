## 2026-07-06 - [ArcGIS FeatureLayer Query Optimization]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, omitting the `out_fields` parameter defaults to retrieving all fields, which can cause significant network load and latency, especially for large datasets.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes when querying web services. Spatial geometry is still safely returned because `returnGeometry` defaults to `True`.

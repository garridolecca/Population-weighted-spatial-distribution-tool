## 2026-07-04 - Optimize FeatureLayer query network load
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency. The `returnGeometry` parameter defaults to `True` in the ArcGIS API, meaning spatial geometry data will still be safely returned alongside the explicitly requested attributes.
**Action:** Always verify if `out_fields` can be utilized when querying `FeatureLayer` objects in ArcGIS scripts.

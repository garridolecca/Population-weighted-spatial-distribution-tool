## 2026-06-28 - [Optimize arcgis FeatureLayer queries with out_fields]
**Learning:** By default, ArcGIS FeatureLayer queries retrieve all attributes. When working with web services, explicitly defining `out_fields` (e.g., to only fetch the population field) significantly reduces payload size and network latency. Spatial data is preserved because `returnGeometry` defaults to `True`.
**Action:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.

## 2026-06-13 - ArcGIS FeatureLayer Query Optimization
**Learning:** By default, arcgis.features.FeatureLayer.query() requests all attributes from the web service. When only a specific field (like a population count) is needed for downstream spatial analysis, this default behavior causes a massive, unnecessary network overhead, fetching demographic attributes we discard.
**Action:** Always explicitly specify the out_fields parameter when calling query() to fetch only required fields, minimizing the network payload and reducing latency.

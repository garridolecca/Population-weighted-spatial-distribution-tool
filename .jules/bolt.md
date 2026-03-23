## 2024-05-18 - [Web Service Query Network Optimization]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, omitting `out_fields` defaults to downloading all attributes. This causes severe network bottlenecks for wide census datasets when only a single population field is needed.
**Action:** Always append `out_fields="<required_fields>"` to `web_layer.query()` calls in ArcPy scripts to limit data retrieval to only necessary attributes, reducing network load and latency.

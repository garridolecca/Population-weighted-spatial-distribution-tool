## 2026-06-06 - [FeatureLayer query out_fields optimization]
**Learning:** In ArcGIS tool development, querying web services like Census data without `out_fields` causes massive performance bottlenecks due to the large number of attributes in census blocks, significantly increasing payload size and network latency.
**Action:** Always specify `out_fields` when using `arcgis.features.FeatureLayer.query()` to fetch only necessary fields.

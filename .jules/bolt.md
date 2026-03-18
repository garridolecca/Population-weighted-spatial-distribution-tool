## 2024-05-24 - [ArcGIS Web Service Query Payload Optimization]
**Learning:** Querying ArcGIS web services via `arcgis.features.FeatureLayer` without specifying `out_fields` downloads all attributes for every returned feature. In large datasets like Census block data, this causes massive network overhead and memory consumption, severely slowing down execution times.
**Action:** Always utilize the `out_fields` parameter in web service queries to fetch only the data strictly necessary for processing, drastically reducing network payload size and latency.

## 2024-05-18 - [Web Layer Queries]
**Learning:** Querying web services without limiting output fields can cause significant performance bottlenecks due to unnecessary data transfer, high latency, and increased memory usage in ArcPy environments.
**Action:** Always use the `out_fields` parameter when querying a `FeatureLayer` via arcgis API to explicitly define the necessary fields.
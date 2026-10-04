## 2026-10-04 - Optimize ArcGIS FeatureLayer.query() Payload
**Learning:** By default, ArcGIS `FeatureLayer.query()` fetches all fields. For wide datasets or large numbers of features, this creates an unnecessarily large payload over the network.
**Action:** When only specific fields are needed from a web service query, always specify the `out_fields` parameter (e.g., `out_fields=population_field`) to minimize the data payload and improve performance.

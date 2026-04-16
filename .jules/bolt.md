## 2026-04-16 - [Optimize FeatureLayer Queries]
**Learning:** By default, `FeatureLayer.query()` retrieves all fields, which can cause significant network latency when querying rich datasets.
**Action:** Always use the `out_fields` parameter in web service queries to fetch only the necessary fields (e.g., the population field) to minimize payload size and improve execution speed.

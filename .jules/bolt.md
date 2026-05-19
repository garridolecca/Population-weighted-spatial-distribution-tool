## 2026-05-19 - [FeatureLayer Web Service Field Limitation]
**Learning:** By default, `arcgis.features.FeatureLayer.query()` requests all fields (`out_fields='*'`), which results in massive network latency and payload sizes when dealing with wide feature services (like Census layers).
**Action:** Always explicitly limit data retrieval by specifying the `out_fields` parameter when querying web services to fetch only the required attributes.

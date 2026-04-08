## 2026-04-08 - [Web Service Network Payload]
**Learning:** When querying web services in ArcGIS (via arcgis.features.FeatureLayer), the default behavior downloads all attributes, which can be hundreds of fields (like in Census data), causing severe network bottlenecks.
**Action:** Always use the `out_fields` parameter to restrict data retrieval to only the necessary fields (e.g., `out_fields=population_field`).

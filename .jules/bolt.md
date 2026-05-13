## 2026-05-13 - [Limit web service payload with out_fields]
**Learning:** When querying ArcGIS web services (`arcgis.features.FeatureLayer`), the default query pulls all attributes, which bloats the network payload and causes significant performance drops, especially for large geographic extents.
**Action:** Always utilize the `out_fields` parameter to explicitly restrict data retrieval to only the necessary fields (e.g., the population field) to minimize network latency.

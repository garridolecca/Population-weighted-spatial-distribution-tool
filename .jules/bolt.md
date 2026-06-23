## 2024-05-24 - [Initialization]
**Learning:** Initializing journal for Bolt.
**Action:** Always read and update this journal.

## 2026-06-23 - [FeatureLayer query optimization]
**Learning:** Querying ArcGIS web services returns all fields by default, which can be a severe performance bottleneck over the network.
**Action:** Always use the `out_fields` parameter when querying `arcgis.features.FeatureLayer` to limit data retrieval to only necessary attributes.

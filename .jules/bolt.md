## 2024-05-24 - [ArcGIS Web Query Optimization]
**Learning:** Fetching full datasets from ArcGIS FeatureLayer Web Services without specifying `out_fields` results in severe payload latency, downloading unnecessary attributes and causing performance bottlenecks.
**Action:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, significantly reducing network load.

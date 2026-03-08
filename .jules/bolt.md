## 2024-05-14 - [Optimize Web Service Query Payload]
**Learning:** When querying ArcGIS web services via `FeatureLayer`, fetching unnecessary attributes introduces significant network load and latency, especially for large geographic extents. The tool only required the geometry and the population field but was fetching the entire attribute table.
**Action:** Always use the `out_fields` parameter in `arcgis.features.FeatureLayer` queries to limit data retrieval to only the necessary attributes.

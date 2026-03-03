## 2026-03-03 - [Selective Field Queries for Web Feature Layers]
**Learning:** `arcgis.features.FeatureLayer` queries return all fields by default, which can be slow and memory-intensive for large datasets. Specifying `out_fields` drastically reduces network load and improves performance.
**Action:** Always use the `out_fields` parameter in web service queries to limit data retrieval to only the necessary attributes.

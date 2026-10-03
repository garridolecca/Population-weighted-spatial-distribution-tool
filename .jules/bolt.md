## 2026-10-03 - Optimize ArcGIS FeatureLayer.query() with out_fields
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. This is inefficient for large datasets like census data where only a single field (like population) is needed. The `returnGeometry` parameter defaults to True, so we don't lose the spatial data.
**Action:** Always specify `out_fields` when querying FeatureLayers to minimize the network payload and speed up the query.

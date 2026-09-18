## 2024-05-24 - ArcGIS FeatureLayer query payload optimization
**Learning:** In ArcGIS toolboxes utilizing `FeatureLayer.query()`, not specifying the `out_fields` parameter causes the API to fetch all fields by default. For wide datasets like census blocks, this creates a massive network bottleneck that slows down processing. Spatial data is safely preserved since `returnGeometry` is True by default.
**Action:** Always optimize `FeatureLayer.query()` calls by explicitly passing only the required fields via the `out_fields` parameter to drastically reduce network payload.

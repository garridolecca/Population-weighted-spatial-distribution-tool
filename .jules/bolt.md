## 2026-10-07 - Optimize ArcGIS FeatureLayer web query network payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. This causes extremely wide datasets (like census data) to load slowly over the network when most fields aren't needed. Using the `out_fields` parameter optimizes the payload significantly by reducing data size returned, while implicit geometry handling keeps spatial data intact.
**Action:** Always specify required `out_fields` when executing remote ArcGIS queries unless all fields are genuinely required, particularly for large or wide layers.

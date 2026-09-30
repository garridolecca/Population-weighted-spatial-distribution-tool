## 2026-09-30 - Optimize ArcGIS FeatureLayer Query
**Learning:** By default, ArcGIS `FeatureLayer.query()` fetches all fields. For wide datasets like census data, this unnecessarily increases network payload and processing time when only spatial intersection and a single population field are needed.
**Action:** Always specify the `out_fields` parameter when querying FeatureLayers to restrict the downloaded attributes to only what is strictly necessary (plus `returnGeometry` is True by default for spatial layers).

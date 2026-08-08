## 2026-08-08 - Optimize ArcGIS FeatureLayer spatial queries
**Learning:** ArcGIS FeatureLayer queries retrieve all fields by default, causing unnecessary network overhead for wide tables (like census data). Specifying `out_fields` is crucial for reducing the API response payload. Note that spatial geometry is returned by default, so we don't need to specify shape fields.
**Action:** Always specify the minimum required fields via the `out_fields` parameter when querying FeatureLayers, especially when handling large geospatial datasets.

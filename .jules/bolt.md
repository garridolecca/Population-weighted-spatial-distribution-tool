## 2026-09-27 - Optimize ArcGIS FeatureLayer.query()
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network overhead and memory usage, especially for wide datasets like Census data.
**Action:** Always specify the required fields using the `out_fields` parameter in `query()`. When fetching geometry (which is the default `returnGeometry=True`), ensure only the strictly necessary attribute fields (like the population field) are requested.

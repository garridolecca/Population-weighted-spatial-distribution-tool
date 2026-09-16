## 2024-09-16 - [Optimize ArcGIS FeatureLayer Web Queries]
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields (`out_fields="*"`). For wide datasets like Census data, this creates massive unnecessary network payloads. Geometry is returned by default, so we only need to request the specific attributes we plan to use.
**Action:** Always explicitly specify `out_fields` when querying ArcGIS web services to minimize payload and parsing time.

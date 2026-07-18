## 2026-07-18 - [Minimize ArcGIS FeatureLayer query payloads]
**Learning:** By default, arcgis.features.FeatureLayer.query() retrieves all fields (`out_fields="*"`). For large datasets like census data, this results in massive network payloads. However, spatial geometry is still safely returned when explicitly limiting `out_fields` because `returnGeometry` defaults to `True`.
**Action:** Always restrict `out_fields` to only the specifically required attribute fields when querying ArcGIS web services to drastically reduce network transfer and memory usage.

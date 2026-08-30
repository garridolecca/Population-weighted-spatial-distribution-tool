## 2026-08-30 - Optimize ArcGIS FeatureLayer Query Payload
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. For wide datasets (like census data), this results in massive, slow network payloads. Additionally, `returnGeometry` defaults to True, so spatial data is still safely returned even when limiting fields.
**Action:** Always specify the required fields using the `out_fields` parameter when performing a `FeatureLayer.query()` to reduce network payload and execution time.

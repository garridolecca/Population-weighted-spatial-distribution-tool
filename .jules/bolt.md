## 2026-07-26 - Optimize ArcGIS FeatureLayer Query Payload
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields (`out_fields='*'`). For wide datasets like census data, this results in unnecessarily large network payloads. The API defaults `returnGeometry=True`, so spatial data is still returned when requesting specific fields.
**Action:** Always specify the required fields using the `out_fields` parameter in `FeatureLayer.query()` to minimize payload size and improve execution speed.

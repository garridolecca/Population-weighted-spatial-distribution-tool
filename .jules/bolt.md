## 2024-09-14 - Optimize arcgis FeatureLayer queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. This can result in massive network payloads for wide datasets (like census data).
**Action:** Always specify the required fields using the `out_fields` parameter (e.g., `out_fields=["P0010001"]`). Geometry is still safely returned as `returnGeometry` defaults to `True`.

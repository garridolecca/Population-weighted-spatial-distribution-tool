## 2026-08-23 - Optimize ArcGIS FeatureLayer query payloads
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network overhead when querying wide datasets like Census blocks.
**Action:** Always specify the minimum required fields using the `out_fields` parameter when calling `query()`. Spatial data will still be safely returned as `returnGeometry` defaults to `True`.

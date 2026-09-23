## 2026-09-23 - Optimize ArcGIS FeatureLayer web queries
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which can cause massive network payloads and latency, especially for wide datasets like Census blocks.
**Action:** Always specify the minimum required fields using the `out_fields` parameter. Spatial geometry will still be safely returned because `returnGeometry` defaults to True.

## 2026-08-17 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause massive network payloads and slow performance on wide datasets (like census blocks). Geometry is returned by default (`returnGeometry=True`), so you only need to request the specific attribute fields required by the tool.
**Action:** Always use the `out_fields` parameter in `query()` to explicitly limit requested attributes when querying FeatureLayers.

## 2026-08-22 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default (equivalent to `SELECT *`). For wide datasets like census blocks, this causes significant network overhead.
**Action:** Always specify the required fields using the `out_fields` parameter when querying `FeatureLayer`s to minimize payload, relying on `returnGeometry=True` defaulting to ensure spatial data is still retrieved.

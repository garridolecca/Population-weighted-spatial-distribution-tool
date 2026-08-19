## 2026-08-19 - Optimize ArcGIS FeatureLayer Queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` fetches all fields. For wide datasets like census data, this creates a massive, unnecessary network payload.
**Action:** Always use the `out_fields` parameter in ArcGIS API queries to request only the specific fields required for the subsequent processing logic (e.g., population).

## 2026-11-09 - ArcGIS FeatureLayer Query Optimization
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default. For wide datasets like Census data, this creates a massive, unnecessary network payload.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when performing spatial queries against feature services.

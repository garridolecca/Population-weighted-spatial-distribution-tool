## 2026-10-19 - Optimize ArcGIS FeatureLayer Queries
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which can cause significant network overhead when querying wide datasets like Census data if only one or two fields are needed. The returnGeometry parameter remains True by default, allowing spatial operations to work even if geometry isn't explicitly requested in out_fields.
**Action:** Always explicitly specify required fields using the out_fields parameter when querying ArcGIS FeatureLayers to minimize payload size and improve performance.

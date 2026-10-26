## 2026-10-26 - ArcGIS FeatureLayer Query Default Payload
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, which creates a massive network payload bottleneck when querying wide datasets like Census data.
**Action:** Always specify the required fields using the out_fields parameter when querying FeatureLayers to minimize network overhead.

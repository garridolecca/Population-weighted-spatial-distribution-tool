## 2026-08-21 - Optimize FeatureLayer Web Query payload
**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default, resulting in bloated network payloads for wide datasets like Census data.
**Action:** Always specify the required fields using the `out_fields` parameter when querying FeatureLayer to reduce network payload, as `returnGeometry` defaults to True.

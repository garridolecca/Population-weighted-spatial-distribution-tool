## 2026-10-01 - Optimize FeatureLayer.query Network Payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause excessive network payloads, especially on wide datasets like census data.
**Action:** Always specify the `out_fields` parameter when only a subset of attributes is needed. `returnGeometry` defaults to True, so spatial operations are unaffected.

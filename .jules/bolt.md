## 2026-08-03 - Optimize FeatureLayer.query payload
**Learning:** ArcGIS FeatureLayer.query fetches all fields by default, which can cause massive network payloads for wide datasets like census blocks.
**Action:** Always specify the required fields using the out_fields parameter to reduce payload size and speed up execution, knowing that returnGeometry defaults to True so spatial data is still safe.

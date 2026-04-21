## 2026-04-21 - [Optimize arcgis FeatureLayer.query]
**Learning:** Web service queries in the `arcgis` API fetch all fields by default, causing large network payloads.
**Action:** Use the `out_fields` parameter to limit returned fields, optimizing the query.

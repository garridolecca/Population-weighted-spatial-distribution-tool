## 2026-04-07 - [Limit FeatureLayer queries with out_fields]
**Learning:** Querying web services without limiting out_fields fetches all attributes, increasing network payload significantly.
**Action:** Always use the out_fields parameter in arcgis.features.FeatureLayer queries to minimize data transfer latency, especially when only one field (like population) is needed.

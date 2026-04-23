## 2026-04-23 - [FeatureLayer query payload optimization]
**Learning:** ArcGIS FeatureLayer.query pulls all attributes by default, causing unnecessary network latency and memory usage when only specific fields are needed.
**Action:** Always use the out_fields parameter in web service queries to restrict downloaded attributes to exactly what is needed for the analysis.

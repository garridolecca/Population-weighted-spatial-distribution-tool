## 2026-04-13 - [Limit Web Service Queries with out_fields]
**Learning:** Querying ArcGIS REST services via arcgis.features.FeatureLayer retrieves all attributes by default, creating a massive network payload and increasing latency, especially with complex census data.
**Action:** Always use the out_fields parameter to explicitly request only the required fields (e.g., population) when making web service queries.

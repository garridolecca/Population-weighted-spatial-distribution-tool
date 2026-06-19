## 2026-06-19 - [FeatureLayer query payload optimization]
**Learning:** When querying web services via arcgis.features.FeatureLayer, requesting all fields by default creates a significant network performance bottleneck. Specifying `out_fields` to limit the payload is a critical codebase-specific optimization.
**Action:** Always utilize the `out_fields` parameter when executing queries against ArcGIS REST services to limit data retrieval to strictly necessary attributes.

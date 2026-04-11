## $(date +%Y-%m-%d) - Limit Web Query Payloads
**Learning:** In ArcGIS tool development, querying web services (`arcgis.features.FeatureLayer`) without specifying `out_fields` can cause large, unnecessary network payloads, increasing memory use and execution time.
**Action:** Always include the `out_fields` parameter in web service queries to fetch only the attributes required by the tool.

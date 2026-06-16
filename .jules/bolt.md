## 2026-06-16 - Limit ArcGIS FeatureLayer query out_fields
**Learning:** By default, arcgis.features.FeatureLayer queries return all fields, resulting in bloated network payloads. When only specific fields (like population density) are needed for local spatial analysis, fetching all data creates a significant bottleneck.
**Action:** Always specify the `out_fields` parameter in web layer queries to restrict data retrieval to only the necessary attributes.

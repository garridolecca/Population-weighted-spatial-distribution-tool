## 2024-03-22 - [Minimize arcgis API network payload using out_fields]
**Learning:** When querying ArcGIS web services via `arcgis.features.FeatureLayer`, requesting only necessary attributes reduces network payload size significantly.
**Action:** Always use the `out_fields` parameter in `.query()` calls when full feature attributes are not required.

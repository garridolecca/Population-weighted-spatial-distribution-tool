## 2026-06-11 - [Limit Web Service Query Attributes]
**Learning:** When querying web services like ArcGIS FeatureLayers, fetching all fields by default creates a massive data transfer payload. Always explicitly use the `out_fields` parameter to restrict data retrieval only to required attributes.
**Action:** Enforce `out_fields` on all `arcgis.features.FeatureLayer.query()` calls to drastically reduce network load and parse time.

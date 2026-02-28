## 2024-05-14 - [FeatureLayer query performance]
**Learning:** When querying web services via arcgis.features.FeatureLayer, the API pulls all fields by default, causing massive network loads.
**Action:** Always use out_fields parameter to restrict fields to what's actually needed (like population fields).

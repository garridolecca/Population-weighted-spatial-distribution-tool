## 2026-07-17 - ArcGIS FeatureLayer Query Optimization
**Learning:** By default, ArcGIS FeatureLayer queries retrieve all fields, which for census block layers can mean hundreds of demographic attributes, causing massive network payloads. However, the spatial geometry is always safely returned even when explicitly restricting attributes.
**Action:** Always specify `out_fields` in `FeatureLayer.query()` calls to pull only the strictly necessary attributes.

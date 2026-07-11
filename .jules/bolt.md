## 2026-07-11 - Optimize ArcGIS FeatureLayer Queries
**Learning:** By default, `FeatureLayer.query()` in the ArcGIS API returns all fields, which can cause bloated network payloads. Setting `out_fields` limits the returned data, while `returnGeometry=True` remains the default, ensuring spatial operations still work.
**Action:** Always restrict `out_fields` to only the required attributes when querying FeatureLayers to minimize network overhead.

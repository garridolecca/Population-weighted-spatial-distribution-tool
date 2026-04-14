## 2026-04-14 - [FeatureLayer Web Query Optimization]
**Learning:** In ArcGIS integrations, querying web services (FeatureLayer) without specifying output fields returns all fields by default, leading to massive unnecessary data downloads (anti-pattern).
**Action:** Always specify the `out_fields` parameter in web layer queries when only specific fields are needed.

## 2026-09-04 - Optimize FeatureLayer web query by specifying out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. When querying wide datasets like Census data for a specific field (like population), this causes massive unnecessary network payloads. Passing `out_fields=population_field` significantly improves download speed while keeping geometries intact since `returnGeometry=True` defaults.
**Action:** Always specify required fields using `out_fields` when querying web layers via ArcGIS API if not all fields are needed.

# Bolt's Journal

## Date: Initial
**Learning:** Initializing journal for Bolt persona.
**Action:** Always document critical codebase-specific performance insights here.

## 2026-08-26 - Optimize FeatureLayer query with out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause significant network payload overhead for wide datasets like census blocks. Adding `out_fields` restricts the payload to only required fields, while spatial geometry data is still safely returned (due to `returnGeometry` defaulting to `True`).
**Action:** Always specify `out_fields` in `FeatureLayer.query()` to minimize network payload unless all fields are explicitly needed.

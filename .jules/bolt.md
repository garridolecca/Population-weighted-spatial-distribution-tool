## 2026-08-10 - Optimize FeatureLayer.query fields
**Learning:** `FeatureLayer.query()` fetches all fields by default. For wide datasets like census, this causes massive network payload overhead.
**Action:** Always use the `out_fields` parameter to restrict downloaded fields to only what is needed.

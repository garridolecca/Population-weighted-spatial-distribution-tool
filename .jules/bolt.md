## 2026-07-29 - Optimize FeatureLayer query by limiting out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, causing massive network payloads for wide datasets like Census data.
**Action:** Always specify `out_fields` to fetch only what's needed. Geometry is returned by default, so it's safe to just request the required attribute fields.

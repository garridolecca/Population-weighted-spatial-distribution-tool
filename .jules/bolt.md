## 2024-05-18 - Initializing Bolt Journal
**Learning:** We need to keep a log of critical performance learnings.
**Action:** Always read this before starting.

## 2026-07-25 - ArcGIS FeatureLayer Network Payload Optimization
**Learning:** By default, `FeatureLayer.query()` fetches all fields (`*`). When querying demographic/census web services containing hundreds of fields, this creates a massive network payload. Setting `out_fields` restricts attributes while still safely returning geometry (since `returnGeometry` defaults to `True`).
**Action:** Always specify `out_fields` when querying ArcGIS feature layers to fetch only explicitly required data.

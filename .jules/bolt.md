## 2026-10-15 - Optimize FeatureLayer queries to fetch only required fields
**Learning:** `FeatureLayer.query()` fetches all fields by default, which can be a huge performance bottleneck (network and memory) for wide datasets like Census blocks.
**Action:** Always specify `out_fields` in `FeatureLayer.query()` when only a subset of attributes is needed.

## 2026-08-14 - Optimize ArcGIS FeatureLayer web query
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, downloading excessive data for wide datasets like census blocks.
**Action:** Explicitly use the `out_fields` parameter when calling `query()` to only fetch required attributes, drastically reducing network payload size.

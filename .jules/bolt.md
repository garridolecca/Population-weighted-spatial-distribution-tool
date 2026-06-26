## 2026-06-26 - [FeatureLayer query performance optimization]
**Learning:** Requesting all attributes from FeatureLayer web queries without using `out_fields` is a performance anti-pattern that causes significant network overhead. Geometry is returned by default, so we only need to request specific fields.
**Action:** Always use the `out_fields` parameter when calling `FeatureLayer.query()` to limit payload size and improve network latency.

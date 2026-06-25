## 2024-06-25 - [Initial Journal]
**Learning:** Initializing journal for Bolt performance learnings.
**Action:** Use this file to record future codebase-specific performance insights.
## 2026-06-25 - [FeatureLayer query optimization]
**Learning:** By default, `FeatureLayer.query()` retrieves all fields from the ArcGIS REST service, which causes significant network bottlenecks when downloading census datasets with many demographic attributes.
**Action:** Always use the `out_fields` parameter to explicitly request only the necessary attributes (e.g., `out_fields=population_field`). Spatial geometry is returned by default (`returnGeometry=True`), so spatial intersects will continue to work.

## 2026-07-13 - [Optimize FeatureLayer Web Queries]
**Learning:** By default, `FeatureLayer.query()` fetches all fields which can result in massive, slow JSON payloads from rich census web services, while `returnGeometry` defaults to `True` anyway.
**Action:** Always restrict `out_fields` to only the explicitly required attributes (e.g., `out_fields=population_field`) when querying web services for spatial analysis.

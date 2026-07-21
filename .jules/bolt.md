## 2026-07-21 - Optimize arcgis FeatureLayer queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` requests all fields. For large datasets like census block geometry, this causes significant unnecessary network overhead when only specific fields are needed. The API safely handles spatial data because `returnGeometry` defaults to True regardless of the `out_fields` requested.
**Action:** Always restrict `out_fields` when querying web services if only a subset of attributes is required.

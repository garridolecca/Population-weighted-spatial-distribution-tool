## 2024-07-09 - Initialization
**Learning:** Initializing bolt journal.
**Action:** Always check for performance improvements!

## 2026-07-09 - Optimize arcgis FeatureLayer queries
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, `returnGeometry` defaults to `True`. Requesting all fields when only one is needed creates a large, unnecessary network payload.
**Action:** Always use the `out_fields` parameter to limit data retrieval to only necessary attributes when using `FeatureLayer.query()`.

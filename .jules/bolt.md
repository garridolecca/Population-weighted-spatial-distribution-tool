## 2026-07-03 - [FeatureLayer Query Performance Pattern]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, retrieving all attributes causes significant network payload bloat. The ArcGIS API safely returns spatial geometry by default (`returnGeometry=True`), allowing us to restrict attributes to just what is needed without losing spatial data.
**Action:** Always use the `out_fields` parameter in `FeatureLayer.query()` calls to limit data retrieval to only necessary attributes (e.g., the population field).

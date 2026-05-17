## 2024-05-17 - [Initialization]
**Learning:** Initializing bolt journal.
**Action:** Always check the journal for previous learnings.

## 2026-05-17 - [Optimize FeatureLayer query out_fields]
**Learning:** By default, arcgis.features.FeatureLayer.query fetches all fields. This can cause significant network payload overhead when only specific fields are needed.
**Action:** Always use the `out_fields` parameter in FeatureLayer queries to limit data retrieval to necessary attributes, reducing network latency and memory usage.

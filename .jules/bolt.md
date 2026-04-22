## 2026-04-22 - [FeatureLayer query performance]
**Learning:** When querying web services via `arcgis.features.FeatureLayer`, always use the `out_fields` parameter to limit data retrieval to only necessary attributes, reducing network load and latency.
**Action:** Ensure `out_fields` is specified on all `FeatureLayer.query()` calls to avoid retrieving massive payloads unnecessarily.

## 2026-05-27 - [FeatureLayer query payload reduction]
**Learning:** Querying web services without specifying `out_fields` retrieves all fields by default, which for census data can be hundreds of columns. This significantly inflates network payload and latency.
**Action:** Always specify `out_fields` when using `FeatureLayer.query()` to retrieve only the required attributes (e.g., the population field) for downstream geoprocessing.

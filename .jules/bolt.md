## 2026-05-14 - Optimize web queries with out_fields
**Learning:** Querying web services via `arcgis.features.FeatureLayer` without specifying `out_fields` retrieves all attributes, which can cause significant network load and latency, especially for large datasets or geometries.
**Action:** Always use the `out_fields` parameter in web queries to limit data retrieval to only the necessary attributes.

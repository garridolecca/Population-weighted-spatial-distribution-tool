## 2026-05-10 - [Reduce Network Payload for Web Service Queries]
**Learning:** Querying ArcGIS feature services without specifying `out_fields` retrieves all attributes, which significantly increases network load and latency, especially for census data which typically has hundreds of fields.
**Action:** Always use the `out_fields` parameter in `FeatureLayer.query()` to fetch only the attributes strictly required for the operation (e.g., the population field).

## 2026-04-25 - FeatureLayer Query Network Payload Optimization
**Learning:** Querying ArcGIS REST services via FeatureLayer without specifying `out_fields` retrieves all attributes for every feature in the extent, causing massive unnecessary network payloads and slowing down data retrieval significantly.
**Action:** Always include `out_fields` with only the required fields (e.g., the population field) when calling `FeatureLayer.query()` to minimize data transfer and latency.

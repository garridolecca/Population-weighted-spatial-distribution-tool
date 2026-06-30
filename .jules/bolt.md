## 2024-07-01 - [Initialization]
**Learning:** Initializing bolt journal.
**Action:** Always document critical learnings.

## 2026-06-30 - [FeatureLayer query payload reduction]
**Learning:** Querying ArcGIS web services without specifying `out_fields` fetches all attributes by default, causing unnecessary network latency and large payloads when only a few fields are needed.
**Action:** Always use the `out_fields` parameter in `FeatureLayer.query` to limit data retrieval to only necessary attributes.

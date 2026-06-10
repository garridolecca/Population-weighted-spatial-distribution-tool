## 2026-06-10 - [Reduce Payload in Web Layer Queries]
**Learning:** Querying ArcGIS feature layers without specifying `out_fields` fetches all attributes by default, causing massive network overhead, especially with complex census datasets.
**Action:** Always use `out_fields` to limit data retrieval to only the necessary fields to minimize network payload and improve query performance.

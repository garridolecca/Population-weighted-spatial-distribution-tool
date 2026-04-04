## 2026-04-04 - [Limit ArcGIS REST API payload size]
**Learning:** ArcGIS REST API featuresets return all attributes by default (acting like `SELECT *`), which is inefficient for Census endpoints with hundreds of columns. `out_fields` should be used to minimize payload.
**Action:** Always include `out_fields` when querying web services to limit data retrieval to only the necessary fields, reducing network load and latency.

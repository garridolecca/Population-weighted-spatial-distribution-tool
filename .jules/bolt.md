## 2026-05-01 - [Limit Web Service Query Output Fields]
**Learning:** Querying ArcGIS REST web services without specifying `out_fields` returns all attributes, significantly increasing network load and latency.
**Action:** Always use the `out_fields` parameter in `FeatureLayer.query()` to retrieve only the necessary attributes (e.g., the population field) when making web service requests.

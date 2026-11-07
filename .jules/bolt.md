## 2026-11-07 - Optimize Wide Feature Layer Queries

**Learning:** ArcGIS FeatureLayer.query() fetches all fields by default. When querying wide datasets like Census data, fetching hundreds of unused columns causes massive unnecessary network payloads and slows down execution.
**Action:** Always explicitly specify the required fields using the `out_fields` parameter when performing feature layer queries to limit data transfer to only what is necessary.

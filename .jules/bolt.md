## 2026-06-22 - [Reduce Web Service Query Payload]
**Learning:** When querying ArcGIS web feature services for specific workflows (like sampling), downloading all default attributes creates an unnecessary network bottleneck.
**Action:** Always specify the `out_fields` parameter in `FeatureLayer.query` to limit the payload to only the attributes strictly required by downstream geoprocessing tools.

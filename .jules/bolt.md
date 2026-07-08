## 2026-07-08 - Optimize Web Service Query Payloads

**Learning:** When querying web services via `arcgis.features.FeatureLayer`, omitting the `out_fields` parameter causes the ArcGIS API to download all feature attributes by default. Since `returnGeometry` defaults to `True`, you can safely specify `out_fields` to fetch only the required attributes along with the spatial data.

**Action:** Always use the `out_fields` parameter when calling `FeatureLayer.query()` over a network to limit the payload to only the fields explicitly needed by the downstream workflow, reducing network latency and memory overhead.

## 2026-08-01 - Optimize Web Layer Queries by Minimizing Payload

**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause severe network bottlenecks when dealing with wide datasets like census data (often containing hundreds of demographic fields).

**Action:** Always specify the `out_fields` parameter in `web_layer.query()` to request only the necessary fields. For spatial sampling, requesting just the population field (while relying on the default `returnGeometry=True`) dramatically reduces the network payload without losing any required geometric or attribute data.

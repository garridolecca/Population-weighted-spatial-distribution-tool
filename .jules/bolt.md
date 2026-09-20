## 2026-09-20 - Optimize FeatureLayer query by specifying out_fields
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census blocks, this results in a large network payload. Specifying `out_fields` reduces the payload size significantly. `returnGeometry` defaults to `True`, so spatial data is still safely returned.
**Action:** Always explicitly specify required fields using `out_fields` when using `FeatureLayer.query()` to minimize network transfer.

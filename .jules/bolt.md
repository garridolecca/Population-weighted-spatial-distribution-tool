## 2026-09-26 - Optimize arcgis FeatureLayer query
**Learning:** `FeatureLayer.query()` fetches all fields by default, causing performance issues. Optimizing it using `out_fields` significantly reduces network payload while spatial geometry data is still returned safely by default.
**Action:** When querying web layers in arcgis, use `out_fields` to specify only necessary fields.

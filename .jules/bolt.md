## 2026-10-06 - Optimize FeatureLayer.query payload
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default, which can cause severe performance issues when querying wide datasets like census blocks. However, spatial geometry is still safely returned even if `out_fields` is explicitly specified.
**Action:** Always specify the minimum required fields (e.g. `out_fields=population_field`) when querying ArcGIS feature layers to reduce network payload and memory footprint without losing essential geometry data.

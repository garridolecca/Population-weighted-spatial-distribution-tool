## 2026-09-02 - Optimize FeatureLayer Queries
**Learning:** ArcGIS `FeatureLayer.query()` fetches all fields by default. For wide datasets like census data, this causes a large network payload and slows down performance. Geometry is safely returned by default alongside explicitly requested attributes.
**Action:** Always specify the required fields using the `out_fields` parameter to reduce payload size and speed up data fetching.

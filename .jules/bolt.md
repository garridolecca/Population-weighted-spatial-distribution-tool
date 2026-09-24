## 2024-05-01 - [ArcGIS FeatureLayer Out Fields]
**Learning:** ArcGIS FeatureLayer query fetches all fields by default which can be very slow for wide datasets (like Census block data)
**Action:** Always specify out_fields in FeatureLayer queries to minimize payload size and improve performance.

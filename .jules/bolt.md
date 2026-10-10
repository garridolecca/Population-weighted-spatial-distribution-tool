## 2026-10-10 - [Optimize FeatureLayer Query Payload by Explicitly Requesting out_fields]
**Learning:** FeatureLayer.query() fetches all fields by default. When working with wide datasets like census blocks, explicitly requesting only the necessary fields (out_fields) drastically reduces the network payload, while spatial geometry is still safely implicitly returned.
**Action:** Always restrict out_fields in web queries for performance, and document that geometry is still preserved in ArcGIS API when doing so.

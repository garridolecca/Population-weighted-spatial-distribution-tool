## 2026-07-16 - [Optimize FeatureLayer Web Queries]
**Learning:** ArcGIS FeatureLayer queries return all fields by default, resulting in bloated payloads when querying census webservices. Restricting fields with out_fields still preserves the geometry because returnGeometry defaults to True.
**Action:** When querying web layers, use out_fields to restrict returned fields to only the ones actually needed.

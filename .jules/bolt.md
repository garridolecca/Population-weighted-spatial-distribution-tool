## 2026-08-04 - Optimize ArcGIS FeatureLayer query out_fields
**Learning:** By default, ArcGIS FeatureLayer.query() fetches all fields from the dataset, which can create a massive network payload when querying wide census datasets over the web. However, spatial geometry (which the tool relies on) is still safely returned even if we restrict the attribute payload, because returnGeometry defaults to True.
**Action:** Always specify the required fields using the out_fields parameter when calling FeatureLayer.query() if you only need a subset of attributes.

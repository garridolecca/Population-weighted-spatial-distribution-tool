## 2026-07-20 - Optimize FeatureLayer Web Query Payload
**Learning:** By default, arcgis.features.FeatureLayer queries pull all fields. If only a specific attribute (and geometry) is needed, specifying `out_fields` drastically reduces payload size over the network. `returnGeometry` defaults to True, so spatial queries are unaffected.
**Action:** Always constrain `out_fields` when querying web services if full feature attribution is not required.

## 2026-05-22 - [Limit web service queries with out_fields]
**Learning:** When using `arcgis.features.FeatureLayer.query()`, omitting the `out_fields` parameter downloads all attributes for every feature, causing massive network payload and high latency, especially for dense census datasets.
**Action:** Always explicitly specify the required fields using `out_fields='field_name'` to limit data retrieval, drastically reducing network load.

## 2026-04-27 - [Optimize Web Query]
**Learning:** When querying web services via arcgis.features.FeatureLayer, fetching all attributes can cause unnecessary network overhead.
**Action:** Use the out_fields parameter to limit data retrieval to only the necessary attributes.

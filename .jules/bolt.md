## 2026-05-06 - Optimize Web Service Queries with out_fields

**Learning:** When querying web services via `arcgis.features.FeatureLayer`, querying without specifying `out_fields` will pull down the entire schema and all attributes, leading to massive unnecessary network payloads, especially for census data which contains hundreds of demographic fields.

**Action:** Always use the `out_fields` parameter in `query()` methods to limit data retrieval to only the explicitly required attributes.

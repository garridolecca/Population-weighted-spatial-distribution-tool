## 2026-05-09 - [Limit FeatureLayer query fields]
**Learning:** Querying ArcGIS FeatureLayers without specifying out_fields fetches all attributes, increasing network load and latency.
**Action:** Always specify the out_fields parameter (e.g., out_fields=[population_field]) when calling FeatureLayer.query() to fetch only required attributes.

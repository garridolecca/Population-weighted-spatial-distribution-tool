## 2026-05-04 - FeatureLayer query optimization
**Learning:** When querying web services via arcgis.features.FeatureLayer without specifying fields, it fetches all attributes. For census block layers, this downloads hundreds of unneeded fields, creating a massive network payload and significant latency.
**Action:** Always use the out_fields parameter to restrict data retrieval to only the necessary fields to drastically reduce payload size and query execution time.

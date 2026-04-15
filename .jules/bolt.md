## 2026-04-15 - [Reduce Web Query Payload with out_fields]
**Learning:** Querying web services without limiting output fields retrieves all attributes, which bloats the network payload and slows down processing, especially for heavy datasets like census blocks.
**Action:** Always use the `out_fields` parameter when querying `arcgis.features.FeatureLayer` to restrict data retrieval to only what is necessary for the tool's execution.

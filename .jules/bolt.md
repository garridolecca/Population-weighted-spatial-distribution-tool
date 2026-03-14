## 2024-03-14 - [FeatureLayer Web Query Optimization]
**Learning:** Querying web services without specifying `out_fields` retrieves all fields. For large datasets like census data with hundreds of fields, this results in significant network latency and memory overhead.
**Action:** Always specify the `out_fields` parameter in `FeatureLayer.query()` to limit data transfer to only the required attributes.

## 2024-03-14 - [Disk I/O Reduction with Memory Workspace]
**Learning:** Writing intermediate geoprocessing results to disk (e.g., a file geodatabase or folder) causes unnecessary disk I/O bottlenecks.
**Action:** Use the `memory` workspace for intermediate feature classes and `arcpy.env.scratchGDB` for temporary persistent files to improve execution speed.

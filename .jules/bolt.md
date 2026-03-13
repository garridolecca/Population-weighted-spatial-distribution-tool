## 2024-05-24 - [ArcGIS FeatureLayer Query Optimization]
**Learning:** Querying `arcgis.features.FeatureLayer` without specifying `out_fields` retrieves all attributes from the service, which causes massive network latency when querying large datasets like Census Blocks. Additionally, storing intermediate feature classes on disk instead of the `memory` workspace introduces unnecessary I/O overhead.
**Action:** Always specify `out_fields=[required_fields]` (e.g., the population field) when making `FeatureLayer.query()` calls to reduce network payload, and use `memory` or `arcpy.env.scratchGDB` workspaces for temporary intermediate data.

## 2024-05-24 - [Optimizing Cleanup Steps in arcpy]
**Learning:** Temporary data cleanup operations (e.g., `arcpy.management.Delete`, `arcpy.management.DeleteField`) are often placed at the end of the `try` block, causing resource leakage if the script fails or returns early. Additionally, failing to verify existence before deletion can throw secondary exceptions during cleanup.
**Action:** Always initialize temporary dataset path variables at the beginning of the `execute` method scope, and relocate cleanup operations to a `finally` block using `arcpy.Exists()` or `arcpy.ListFields()` to verify existence before deletion.

## 2026-02-25 - [ArcGIS Input Modification Anti-Pattern]
**Learning:** The codebase modifies the input dataset in-place (adding/calculating/deleting fields) to perform attribute transfer. This is a severe performance bottleneck (schema locks, disk I/O) and a data integrity risk (if the tool fails, fields remain).
**Action:** In future optimizations, prioritize replacing such logic with 'arcpy.da.SearchCursor' and 'arcpy.da.InsertCursor' to handle data transfer in memory without modifying the source schema.

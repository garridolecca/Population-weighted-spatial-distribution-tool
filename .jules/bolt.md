## 2024-05-18 - [Initial Learnings]
**Learning:** This is a fresh start. Need to find the primary tools/bottlenecks.
**Action:** Explore the codebase first.

## 2026-06-27 - [Network Optimization]
**Learning:** Querying `arcgis.features.FeatureLayer` without specifying `out_fields` retrieves all attributes by default, creating massive unnecessary network loads for census data.
**Action:** Always specify `out_fields` to limit data retrieval to only the necessary fields.

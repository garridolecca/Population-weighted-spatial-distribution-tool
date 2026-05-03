## 2026-05-03 - [Initial Bolt Setup]
**Learning:** Initializing bolt.md for performance tracking in IntelligentDistribution_v2.
**Action:** Always document critical learnings here.
## 2026-05-03 - [Web Service Query Optimization]
**Learning:** Retrieving all fields from a web service query incurs unnecessary network load and latency. Using the `out_fields` parameter limits the data retrieval to only what is needed.
**Action:** Always use the `out_fields` parameter in `FeatureLayer.query()` calls to limit data payload.

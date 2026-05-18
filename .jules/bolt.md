## 2026-05-18 - [FeatureLayer query performance improvement]
**Learning:** Found a performance bottleneck when using `arcgis.features.FeatureLayer.query()` in the "Use Web Service" option of the Python Toolbox. It queries without specifying `out_fields`, pulling down all attributes for every feature over the network, which is very inefficient, especially when only one field (`population_field`) is needed.
**Action:** Always use `out_fields=[population_field]` when querying web services to limit data transfer.

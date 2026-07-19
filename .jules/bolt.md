## 2026-07-19 - Optimize Web Service Payload Size
**Learning:** Querying Census Web Services via `arcgis.features.FeatureLayer.query()` without specifying `out_fields` defaults to requesting all attributes (`*`), causing massive unneeded payload downloads. By explicitly restricting it to just the required `population_field`, performance significantly improves while maintaining the spatial geometry.
**Action:** Always specify `out_fields` when querying web feature layers to only return required attributes, unless all fields are explicitly needed.

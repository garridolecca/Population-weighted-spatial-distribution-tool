## 2026-07-23 - Optimize ArcGIS FeatureLayer web queries
**Learning:** By default, `arcgis.features.FeatureLayer.query()` retrieves all fields (attributes) from the server. When querying large datasets like Census block layers, this causes significant unnecessary network payload and memory usage.
**Action:** Always explicitly specify the `out_fields` parameter when using `web_layer.query()` to only fetch the exact fields required by the script.

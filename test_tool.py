import sys
import unittest
from unittest.mock import MagicMock, ANY

sys.modules['arcpy'] = MagicMock()
sys.modules['arcpy.management'] = MagicMock()
sys.modules['arcpy.analysis'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

import importlib.machinery
import importlib.util
loader = importlib.machinery.SourceFileLoader('intel_v2', 'IntelligentDistribution_v2.pyt')
spec = importlib.util.spec_from_loader(loader.name, loader)
intel_v2 = importlib.util.module_from_spec(spec)
loader.exec_module(intel_v2)

class TestIntelTool(unittest.TestCase):
    def test_execute_web_service(self):
        tool = intel_v2.DistributePointsByPopulation()

        intel_v2.arcpy = sys.modules['arcpy']
        intel_v2.GIS = sys.modules['arcgis.gis'].GIS
        intel_v2.FeatureLayer = sys.modules['arcgis.features'].FeatureLayer

        params = [MagicMock() for _ in range(7)]
        params[0].valueAsText = "MOCK_STRING"
        params[1].valueAsText = "MOCK_STRING"
        params[2].valueAsText = "MOCK_STRING"
        params[3].valueAsText = "Use Web Service"
        params[4].valueAsText = "MOCK_STRING"
        params[5].valueAsText = "MOCK_STRING"
        params[6].valueAsText = "MOCK_STRING"

        messages = MagicMock()

        desc_mock = MagicMock()
        desc_mock.extent.XMin = 0
        desc_mock.extent.YMin = 0
        desc_mock.extent.XMax = 10
        desc_mock.extent.YMax = 10
        desc_mock.extent.spatialReference.factoryCode = 4326
        intel_v2.arcpy.Describe.return_value = desc_mock

        featureset_mock = MagicMock()
        featureset_mock.features = [MagicMock()]
        intel_v2.FeatureLayer.return_value.query.return_value = featureset_mock

        intel_v2.arcpy.management.GetCount.return_value.getOutput.return_value = 1

        field_mock = MagicMock()
        field_mock.name = "TestField"
        field_mock.required = False
        intel_v2.arcpy.ListFields.return_value = [field_mock]

        tool.execute(params, messages)

        intel_v2.FeatureLayer.return_value.query.assert_called_with(
            geometry_filter=ANY,
            out_fields="MOCK_STRING"
        )

if __name__ == '__main__':
    unittest.main()

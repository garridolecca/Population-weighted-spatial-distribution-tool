import unittest
import sys
import types
import os
from unittest.mock import MagicMock

# Mock arcpy and arcgis before importing the toolbox
sys.modules['arcpy'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

def load_pyt_as_module(path):
    with open(path, 'r') as f:
        code = f.read()
    module = types.ModuleType("toolbox")
    module.__file__ = path
    exec(code, module.__dict__)
    return module

class TestDistributePointsByPopulation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Path to the .pyt file relative to the root
        pyt_path = os.path.join(os.path.dirname(__file__), '..', 'IntelligentDistribution_v2.pyt')
        cls.module = load_pyt_as_module(pyt_path)

    def setUp(self):
        self.tool = self.module.DistributePointsByPopulation()

    def test_updateParameters_local_census(self):
        """Test updateParameters when census_source_choice is 'Use Local Census Layer'."""
        # Create mock parameters
        # param3: census_source_choice
        # param4: in_local_census
        # param5: in_web_census_url
        params = [MagicMock() for _ in range(7)]
        params[3].valueAsText = "Use Local Census Layer"

        # Initialize enabled states to ensure they actually change
        params[4].enabled = False
        params[5].enabled = True

        # Call the method
        self.tool.updateParameters(params)

        # Verify changes
        self.assertTrue(params[4].enabled, "Local census layer should be enabled")
        self.assertFalse(params[5].enabled, "Web census URL should be disabled")

    def test_updateParameters_web_service(self):
        """Test updateParameters when census_source_choice is 'Use Web Service'."""
        # Create mock parameters
        params = [MagicMock() for _ in range(7)]
        params[3].valueAsText = "Use Web Service"

        # Initialize enabled states to ensure they actually change
        params[4].enabled = True
        params[5].enabled = False

        # Call the method
        self.tool.updateParameters(params)

        # Verify changes
        self.assertFalse(params[4].enabled, "Local census layer should be disabled")
        self.assertTrue(params[5].enabled, "Web census URL should be enabled")

    def test_updateParameters_other_value(self):
        """Test updateParameters when census_source_choice is something else (no changes expected)."""
        # Create mock parameters
        params = [MagicMock() for _ in range(7)]
        params[3].valueAsText = "Unknown Choice"

        # Initialize enabled states
        params[4].enabled = True
        params[5].enabled = True

        # Call the method
        self.tool.updateParameters(params)

        # Verify NO changes
        self.assertTrue(params[4].enabled)
        self.assertTrue(params[5].enabled)

if __name__ == '__main__':
    unittest.main()

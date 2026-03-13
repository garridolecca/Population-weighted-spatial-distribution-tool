import sys
import types
from unittest.mock import MagicMock

# Mock arcpy and arcgis modules
sys.modules['arcpy'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

# Load the .pyt file
pyt_module = types.ModuleType('IntelligentDistribution_v2')
with open('IntelligentDistribution_v2.pyt', 'r') as f:
    exec(f.read(), pyt_module.__dict__)

# Instantiate toolbox and tool
toolbox = pyt_module.Toolbox()
print(f"Toolbox Label: {toolbox.label}")
tool = pyt_module.DistributePointsByPopulation()
print(f"Tool Label: {tool.label}")
params = tool.getParameterInfo()
print(f"Number of parameters: {len(params)}")

print("Mock load test passed successfully!")

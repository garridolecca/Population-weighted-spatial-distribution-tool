import sys
from unittest.mock import MagicMock
import types

# Mock required arcpy and arcgis modules
sys.modules['arcpy'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

# Create a module object
pyt_module = types.ModuleType("IntelligentDistribution_v2")

# Read the file content and execute it within the new module
with open("IntelligentDistribution_v2.pyt", "r") as f:
    exec(f.read(), pyt_module.__dict__)

# Instantiate toolbox and tool to verify basic structural integrity
try:
    toolbox = pyt_module.Toolbox()
    tool = pyt_module.DistributePointsByPopulation()
    print("Successfully instantiated Toolbox and DistributePointsByPopulation.")

    # Try calling getParameterInfo to verify it works
    params = tool.getParameterInfo()
    print(f"Successfully retrieved {len(params)} parameters.")
except Exception as e:
    print(f"Error during instantiation or method call: {e}")
    sys.exit(1)

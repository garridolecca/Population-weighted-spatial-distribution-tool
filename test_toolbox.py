import sys
from unittest.mock import MagicMock

# Mock necessary modules
sys.modules['arcpy'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

# Load the toolbox file
try:
    with open('IntelligentDistribution_v2.pyt', 'r') as file:
        code = file.read()

    # Create a new module space to exec the code
    import types
    module = types.ModuleType('toolbox')
    exec(code, module.__dict__)

    # Check if the toolbox class exists
    if hasattr(module, 'Toolbox'):
        print("Successfully loaded IntelligentDistribution_v2.pyt")
        tb = module.Toolbox()
        tool = tb.tools[0]()
        params = tool.getParameterInfo()
        print(f"Tool loaded with {len(params)} parameters.")
    else:
        print("Failed to find Toolbox class.")
except Exception as e:
    print(f"Error executing toolbox code: {e}")

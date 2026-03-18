import sys
import types
from unittest.mock import MagicMock

# Mock required modules
sys.modules['arcpy'] = MagicMock()
sys.modules['arcgis'] = MagicMock()
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

# Now we can mock specific things we might need to test execution
import arcpy

class DummyParameter:
    def __init__(self, valueAsText):
        self.valueAsText = valueAsText

# Set up mock parameters for the test
params = [
    DummyParameter("in_points_fc"),
    DummyParameter("in_aoi_fc"),
    DummyParameter("out_features_fc"),
    DummyParameter("Use Web Service"),
    DummyParameter("local_census_fc"),
    DummyParameter("web_census_url"),
    DummyParameter("P0010001") # population_field
]

class DummyMessages:
    def addMessage(self, msg):
        print(f"[Message] {msg}")
    def addError(self, msg):
        print(f"[Error] {msg}")
    def addWarning(self, msg):
        print(f"[Warning] {msg}")

messages = DummyMessages()

# Read and execute the toolbox file
try:
    with open('IntelligentDistribution_v2.pyt', 'r') as f:
        code = f.read()

    # Create a dummy module to run the code in
    toolbox_module = types.ModuleType('toolbox_module')
    exec(code, toolbox_module.__dict__)

    print("Toolbox loaded successfully.")

    # Check if we can instantiate it and access the tool
    toolbox = toolbox_module.Toolbox()
    print(f"Loaded toolbox: {toolbox.label}")

    tool_class = toolbox.tools[0]
    tool_instance = tool_class()
    print(f"Loaded tool: {tool_instance.label}")

    print("Trying to execute the tool logic...")

    # Let's mock the GIS and query to make sure it doesn't actually try to hit anything
    mock_gis = MagicMock()
    mock_featurelayer = MagicMock()
    mock_featureset = MagicMock()
    mock_featureset.features = [1, 2, 3] # non-empty feature set
    mock_featurelayer.query.return_value = mock_featureset

    toolbox_module.GIS = MagicMock(return_value=mock_gis)
    toolbox_module.FeatureLayer = MagicMock(return_value=mock_featurelayer)

    # Execute the tool
    tool_instance.execute(params, messages)

    # Verify our query was called with out_fields
    mock_featurelayer.query.assert_called_once()
    kwargs = mock_featurelayer.query.call_args[1]

    assert "out_fields" in kwargs, "out_fields was not passed to query!"
    assert kwargs["out_fields"] == "P0010001", f"Expected out_fields='P0010001', got {kwargs['out_fields']}"

    print("Optimization verified successfully!")

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

print("All tests passed.")

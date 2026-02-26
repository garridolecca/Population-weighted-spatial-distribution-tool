
import sys
import unittest
from unittest.mock import MagicMock, call
import types

# --- Setup Mocks ---
arcpy = MagicMock()
sys.modules['arcpy'] = arcpy
sys.modules['arcpy.da'] = MagicMock()
sys.modules['arcpy.management'] = MagicMock()
sys.modules['arcpy.analysis'] = MagicMock()

# Mock arcgis
arcgis = MagicMock()
sys.modules['arcgis'] = arcgis
sys.modules['arcgis.gis'] = MagicMock()
sys.modules['arcgis.features'] = MagicMock()

# --- Load Tool ---
pyt_path = 'IntelligentDistribution_v2.pyt'
with open(pyt_path, 'r') as f:
    code = f.read()

mod = types.ModuleType('IntelligentDistribution_v2')
sys.modules['IntelligentDistribution_v2'] = mod
exec(code, mod.__dict__)

class TestOptimization(unittest.TestCase):
    def setUp(self):
        self.tool = mod.DistributePointsByPopulation()
        # Reset mocks
        arcpy.reset_mock()
        arcpy.management.reset_mock()
        arcpy.da.reset_mock()

    def test_cursor_implementation(self):
        # Mock setup for execution
        arcpy.GetMessages.return_value = "Messages"
        arcpy.Describe.return_value.OIDFieldName = "OBJECTID"
        arcpy.Describe.return_value.shapeFieldName = "Shape"
        arcpy.management.GetCount.return_value.getOutput.return_value = "10"

        # Mock ListFields to return some fields
        field1 = MagicMock()
        field1.name = "Field1"
        field1.type = "String"
        field1.length = 50
        field1.required = False
        field1.isNullable = True

        field2 = MagicMock()
        field2.name = "OBJECTID"
        field2.type = "OID"
        field2.required = True

        field3 = MagicMock()
        field3.name = "Shape"
        field3.type = "Geometry"
        field3.required = True

        arcpy.ListFields.return_value = [field1, field2, field3]

        # Mock Cursors
        search_cursor_mock = MagicMock()
        update_cursor_mock = MagicMock()

        # Simulate rows
        search_cursor_mock.__iter__.return_value = [("Value1",), ("Value2",)]
        update_cursor_mock.__iter__.return_value = [("OldValue1",), ("OldValue2",)]

        arcpy.da.SearchCursor.return_value = search_cursor_mock
        arcpy.da.UpdateCursor.return_value = update_cursor_mock

        # Parameters
        params = [
            MagicMock(valueAsText="in_points"),
            MagicMock(valueAsText="in_aoi"),
            MagicMock(valueAsText="out_points"),
            MagicMock(valueAsText="Use Local Census Layer"),
            MagicMock(valueAsText="local_census"),
            MagicMock(valueAsText="http://url"),
            MagicMock(valueAsText="POP"),
        ]

        messages = MagicMock()
        self.tool.execute(params, messages)

        # --- VERIFICATION ---

        # 1. Verify NO input modification (AddField/CalculateField/JoinField on "in_points")
        # In the OLD code, AddField is called on in_points_fc
        # In the NEW code, it should NOT be called on in_points_fc

        # Check calls to AddField
        # We expect AddField to be called on 'out_points' for 'Field1', but NOT 'in_points'
        add_field_calls = arcpy.management.AddField.call_args_list
        # Filter calls where the first arg is "in_points"
        in_points_modifications = [c for c in add_field_calls if c[0][0] == "in_points"]

        if in_points_modifications:
            print("FAIL: Input dataset was modified (AddField called on in_points)")
            for call_args in in_points_modifications:
                print(f"  Called with: {call_args}")
        else:
            print("PASS: Input dataset was NOT modified by AddField")

        # Check JoinField
        join_calls = arcpy.management.JoinField.call_args_list
        if join_calls:
            print("FAIL: JoinField was called (Old method still in use)")
        else:
            print("PASS: JoinField was NOT called")

        # Check Cursors Usage
        # We expect SearchCursor on in_points and UpdateCursor on out_points
        arcpy.da.SearchCursor.assert_called()
        print("PASS: SearchCursor was used")
        arcpy.da.UpdateCursor.assert_called()
        print("PASS: UpdateCursor was used")

if __name__ == '__main__':
    unittest.main()

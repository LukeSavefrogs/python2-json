import unittest

import json

class BaseTestCase(unittest.TestCase):
    def test_string(self):
        self.assertEqual(
            json.dumps("string"),
            '"string"',
            "Strings should work"
        )
        
    def test_null(self):
        self.assertEqual(
            json.dumps(None),
            'null',
            "Null object should work"
        )
        
    def test_numbers(self):
        self.assertEqual(
            json.dumps(157),
            '157',
            "Integer numbers should work"
        )
        self.assertEqual(
            json.dumps(3.14),
            '3.14',
            "Floating point numbers should work"
        )
        self.assertEqual(
            json.dumps(3.14e10),
            '31400000000.0',
            "Exponential numbers should work"
        )

    def test_bool(self):
        self.assertEqual(
            json.dumps(True),
            "true"
        )
        self.assertEqual(
            json.dumps(False),
            "false"
        )

    def test_custom_bool(self):
        self.assertEqual(
            json.dumps("__TEST_TRUE__", truthy_value="__TEST_TRUE__", falsy_value="__TEST_FALSE__"),
            'true'
        )
        self.assertEqual(
            json.dumps("__TEST_FALSE__", truthy_value="__TEST_TRUE__", falsy_value="__TEST_FALSE__"),
            'false'
        )


class ArrayTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(json.dumps([]), '[]')
    
    def test_simple(self):
        self.assertEqual(
            json.dumps(["", "test1", "", "test2", ""]),
            '["", "test1", "", "test2", ""]'
        )

        
# 	def test_ (self):
# 		json.dumps( 
# 			{
# 				"string": "value",
# 				"string_too": "2",
# 				"boolean": True,
# 				"integer_or_boolean": 0,
# 				"integer": 14,
# 				"float": 27.3,
# 				"null": None,
# 			}, 
# 			'{"string": "value","string_too": "2","boolean": true,"integer_or_boolean": 0,"integer": 14,"float": 27.3,"null": null}'
# 		)
    
# 	def test_ (self):
# 		json.dumps( 
#         {
#             "string": "value",
#             "string_too": "2",
#             "boolean": True,
#             "integer_or_boolean": 0,
#             "integer": 14,
#             "float": 27.3,
#             "null": None,
#         }, 
#         '{"string": "value","string_too": "2","boolean": true,"integer_or_boolean": false,"integer": 14,"float": 27.3,"null": null}', 
#         None, 
#         truthy_value=1, falsy_value=0
#     )
    
# 	def test_ (self):
# 		json.dumps( 
#         {
#             "string": "value",
#             "string_too": "2",
#             "boolean": True,
#             "integer_or_boolean": 0,
#             "integer": 14,
#             "float": 27.3,
#             "null": None,
#         }, 
#         '''{
#     "string": "value",
#     "string_too": "2",
#     "boolean": true,
#     "integer_or_boolean": 0,
#     "integer": 14,
#     "float": 27.3,
#     "null": null
# }''', 
#         4
#     )
    
# 	def test_ (self):
# 		json.dumps( 
#         {
#             "string": "value",
#             "string_too": "2",
#             "boolean": True,
#             "integer_or_boolean": 0,
#             "integer": 14,
#             "float": 27.3,
#             "null": None,
#         }, 
#         '''{
#     "string": "value",
#     "string_too": "2",
#     "boolean": true,
#     "integer_or_boolean": false,
#     "integer": 14,
#     "float": 27.3,
#     "null": null
# }''', 
#         4,
#         truthy_value=1, falsy_value=0
#     )
    
    
# 	def test_ (self):
# 		json.dumps(
#         {
#             "string": "value",
#             "dict": {
#                 "nested_key": "nested_value",
#                 "test": 1
#             }
#         }, 
#         '{"string": "value","dict": {"nested_key": "nested_value","test": true}}', 
#         None, 
#         truthy_value=1, falsy_value=0
#     )
    
# 	def test_ (self):
# 		json.dumps( {
#         "string": "value",
#         "dict": {
#             "nested_key": "nested_value",
#             "list": [
#                 {"list_object": "value1"},
#                 ["value2"],
#                 "value3",
#             ]
#         }
#     }, '''{
#     "string": "value",
#     "dict": {
#         "nested_key": "nested_value",
#         "list": [
#             {
#                 "list_object": "value1"
#             },
#             [
#                 "value2"
#             ],
#             "value3"
#         ]
#     }
# }''',
#         4, 
#         truthy_value=1, falsy_value=0
#     )




if __name__ == '__main__':
    unittest.main(verbosity=2)
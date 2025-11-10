import unittest
from uml_class import UMLClass

class TestUMLClass(unittest.TestCase):

    def setUp(self):
        self.uml = UMLClass("Student")

    # 1
    def test_constructor_valid_name(self):
        self.assertEqual(self.uml.get_name(), "Student")

    # 2
    def test_constructor_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            UMLClass("")

    # 3
    def test_set_name_valid(self):
        self.uml.set_name("Teacher")
        self.assertEqual(self.uml.get_name(), "Teacher")

    # 4
    def test_set_name_invalid_raises(self):
        with self.assertRaises(ValueError):
            self.uml.set_name(" ")

    # 5
    def test_add_attribute_valid(self):
        self.uml.add_attribute("age")
        self.assertIn("age", self.uml.get_attributes())

    # 6
    def test_add_attribute_invalid_raises(self):
        with self.assertRaises(ValueError):
            self.uml.add_attribute("")

    # 7
    def test_add_method_valid(self):
        self.uml.add_method("get_name()")
        self.assertIn("get_name()", self.uml.get_methods())

    # 8
    def test_add_method_invalid_raises(self):
        with self.assertRaises(ValueError):
            self.uml.add_method(None)

    # 9
    def test_get_attributes_returns_list(self):
        self.assertIsInstance(self.uml.get_attributes(), list)

    # 10
    def test_get_methods_returns_list(self):
        self.assertIsInstance(self.uml.get_methods(), list)

    # 11
    def test_attributes_initially_empty(self):
        self.assertEqual(len(self.uml.get_attributes()), 0)

    # 12
    def test_methods_initially_empty(self):
        self.assertEqual(len(self.uml.get_methods()), 0)


if __name__ == '__main__':
    unittest.main()

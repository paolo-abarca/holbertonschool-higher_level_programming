#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models.base import Base
from models.base import __doc__ as module_doc
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """
    The class testbase
    functionality
    """
    def test_docstrings(self):
        """
        Test for docstrings
        """
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_base(self):
        """
        Test for id property
        """
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)
        self.b2 = Base()
        self.assertEqual(self.b2.id, 2)
        self.b3 = Base(30)
        self.assertEqual(self.b3.id, 30)
        self.b4 = Base(25)
        self.assertEqual(self.b4.id, 25)
        self.b5 = Base()
        self.assertEqual(self.b5.id, 3)

    def test_to_from_json_string(self):
        """
        Test for to_from_json_string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(r1_dict, {'x': 2,
                                   'width': 10,
                                   'id': 1,
                                   'height': 7,
                                   'y': 8})
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(json_dict), str)
        self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                           '"width": 10, '
                                                           '"id": 1, '
                                                           '"height": 7, '
                                                           '"y": 8}]'))
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIs(type(json_list_input), str)
        self.assertIs(type(list_output), list)
        self.assertEqual(list_output, list_input)
        self.assertEqual(json.loads(json_list_input),
                         json.loads('[{"height": 4, '
                                    '"width": 10, '
                                    '"id": 89}, '
                                    '{"height": 7, '
                                    '"width": 1, '
                                    '"id": 7}]'))

    def test_save_to_file(self):
        """
        Test for save_to_file
        """
        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))

    def test_from_json_string(self):
        """
        Test for from_json_string
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertCountEqual(list_output, res)
        self.assertEqual(type(list_output), list)

        list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(list_output_1, [])

        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output_2, [])

    def test_create(self):
        """
        Test for create
        """
        r1 = Rectangle(3, 5, 1, 2, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (10) 1/2 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (10) 1/2 - 3/5")
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """
        Test for load_from_file
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))


if __name__ == "__main__":
    unittest.main()

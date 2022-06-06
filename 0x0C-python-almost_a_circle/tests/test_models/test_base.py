#!/usr/bin/python3
"""
Unittest Class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json


class TestBase(unittest.TestCase):
    """
    the test Base
    """
    def task1(self):
        """
        method test for task1
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def task15(self):
        """
        method test for task15
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertNotEqual(json_dictionary, '[{"width": 10, "height": 7,\
        "x": 2, "y": 8, "id": 3}]')

    def task16(self):
        """
        method test for task16
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        s1 = Square(6, 5, 3)
        s2 = Square(9)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))

        contenido3 = []
        Base.save_to_file(None)
        with open("Base.json", encoding="utf-8") as Myfile2:
            contenido3 = Myfile2.read()
        contenido3_dict = json.loads(contenido3)
        j3_string = []
        self.assertEqual(contenido3_dict, j3_string)

        contenido4 = []
        Base.save_to_file("")
        with open("Base.json", encoding="utf-8") as Myfile3:
            contenido4 = Myfile3.read()
        contenido4_dict = json.loads(contenido4)
        j4_string = []
        self.assertEqual(contenido4_dict, j4_string)

    def task17(self):
        """
        method test for task17
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = json.dumps(list_input)
        list_output = json.loads(json_list_input)
        self.assertEqual(list_output, list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(type(list_output[0]), dict)
        self.assertEqual(type(json_list_input), str)

        list1 = []
        self.assertEqual(list1, Base.from_json_string(None))

    def task18(self):
        """
        method test for task18
        """
        x1d = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        xr2 = Rectangle.create(**x1d)
        self.assertDictEqual(x1d, xr2.to_dictionary())

        s1d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        sr2 = Square.create(**s1d)
        self.assertDictEqual(s1d, sr2.to_dictionary())

    def task19(self):
        """
        method test for task19
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        listentry = [r1, r2]
        Rectangle.save_to_file(listentry)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(listentry[0]), id(list_out[0]))
        self.assertEqual(str(listentry[1]), '[Rectangle] (4) 0/0 - 2/4')

        s100 = Square(5)
        s200 = Square(7, 9, 1)
        listentry2 = [s100, s200]
        Square.save_to_file(listentry2)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(listentry2[0]), id(list_out[0]))
        self.assertEqual(str(listentry2[0]), '[Square] (7) 0/0 - 5')
        self.assertEqual(str(listentry2[1]), '[Square] (8) 9/1 - 7')

    if __name__ == "__main__":
        unittest.main()

#!/usr/bin/python3
"""
This class will be the “base”
of all other classes in this project.
"""
import json
import os
import csv


class Base:
    """
    The class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of arguments
        the class Base
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method def to_json_string(list_dictionaries):
        which returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        else:
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method save_to_file(cls, list_objs):
        which writes the JSON string representation of
        list_objs to a file
        """
        filename = cls.__name__ + ".json"
        string = []
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write(cls.to_json_string(string))

            else:
                for i in list_objs:
                    string.append(cls.to_dictionary(i))

                f.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        static method def from_json_string(json_string):
        which returns the list of the JSON string representation
        json_string
        """
        if json_string is None or len(json_string) == 0:
            return []

        else:
            list_json = json.loads(json_string)
            return list_json

    @classmethod
    def create(cls, **dictionary):
        """
        class method def create(cls, **dictionary):
        which returns an instance with all attributes
        already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method def load_from_file(cls):
        which returns a
        list of instances
        """
        list_ = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                dictionary = cls.from_json_string(f.read())

            for i in dictionary:
                list_.append(cls.create(**i))

            return list_

        else:
            return list_

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method save_to_file_csv(cls, list_objs):
        which writes the JSON string representation of
        list_objs to a file
        """
        filename = cls.__name__ + ".csv"
        string = "[]"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write(string)

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]

                write = csv.DictWriter(f, fieldnames=fieldnames)

                for i in list_objs:
                    write.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        class method load_from_file_csv(cls):
        that serializes and deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        string = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                read = csv.reader(f, delimiter=',')

                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]

                if cls.__name__ == "Square":
                    field = ["id", "size", "x", "y"]

                for j, k in enumerate(read):
                    if j > 0:
                        i = cls(1, 1)

                        for o, m in enumerate(k):
                            if m:
                                setattr(i, field[o], int(m))

                        string.append(i)

        return string

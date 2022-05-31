#!/usr/bin/python3
"""
Write a class MyInt that
inherits from int
"""


class MyInt(int):
    """
    class MyInt inherits from int
    """

    def __eq__(self, other):
        """
        function eq return ne
        """
        return super().__ne__(self)

    def __ne__(self, other):
        """
        function ne return eq
        """
        return super().__eq__(self)

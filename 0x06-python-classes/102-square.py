#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and its size and checking
if the given values are right, and a setter and getter methods to set or get
it. Some equivalence methods are present to help handles the use of
comparators. There's also an area method that returns the area of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        """
        self.size = size

    def __eq__(self, other):
        """Sets the compare equality behavior of the Square object.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Sets the compare less than behavior of the Square object.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behavior of the Square object.
        Args:
            other (Square): the Square object to compare with.
        """
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

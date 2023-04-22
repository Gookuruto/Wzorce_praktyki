"""
Liskov substitution princliple
Objects of a superclass should be
able to replace objects of a subclass, without altering the correctness of the program.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height


def use_it(rc):
    w = rc.width
    rc.set_height(10)
    assert rc.get_area() == w * 10


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5, 5)
use_it(sq)

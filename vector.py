from math import *
from numbers import Number


class Vector:
    def __init__(self, x, y, polar=False):
        if polar:
            self.dir = x
            self.mag = y
            self.x = self.get_x()
            self.y = self.get_y()
        else:
            self.x = x
            self.y = y
            self.dir = self.get_dir()
            self.mag = self.get_mag()

    def get_dir(self):
        return atan2(self.y, self.x)

    def get_mag(self):
        return hypot(self.x, self.y)

    def get_x(self):
        return cos(self.x) * self.mag

    def get_y(self):
        return sin(self.y) * self.mag

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector(self.x*other, self.y*other)
        else:
            raise Exception("Not a valid multiplication scalar for Vectors")

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

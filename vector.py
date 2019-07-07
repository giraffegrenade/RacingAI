from math import *
from numbers import Number
from util import *


class Vector:
    def __init__(self, x, y, polar=False):
        if polar:
            self.direction = x
            self.mag = y
            self.x = self.get_x()
            self.y = self.get_y()
        else:
            self.x = x
            self.y = y
            self.direction = self.get_dir()
            self.mag = self.get_mag()

    def get_dir(self):
        return atan2(self.y, self.x)

    def get_mag(self):
        return hypot(self.x, self.y)

    def get_x(self):
        return cos(self.direction) * self.mag

    def get_y(self):
        return sin(self.direction) * self.mag

    def set_dir(self, value):
        self.direction = value
        self.mag = self.get_mag()
        self.x = self.get_x()
        self.y = self.get_y()

    def set_mag(self, value):
        self.mag = value
        self.direction = self.get_dir()
        self.x = self.get_x()
        self.y = self.get_y()

    def normalize(self):
        return Vector(cos(self.direction), sin(self.direction))

    def clamp(self, mag):
        return mag * self.normalize()

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector(self.x*other, self.y*other)
        else:
            raise Exception("Not a valid multiplication scalar for Vectors")

    def __rmul__(self, other):
        if isinstance(other, Number):
            return Vector(self.x*other, self.y*other)
        else:
            raise Exception("Not a valid multiplication scalar for Vectors")

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y

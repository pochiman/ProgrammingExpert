##### Shape Interface #####

# Complete the Square and Circle class such that they properly implement the Shape interface.

# The perimeter of a circle is it's circumference which is given by the formula 2 * pi * radius.
# To obtain pi, you can use math.pi from python's math module.

# The area of a circle is given by the formula pi * (radius ** 2).

# If you have implemented the interface properly, the pre-written driver cpde should output True.

import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError


class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return self.side_length * 4


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
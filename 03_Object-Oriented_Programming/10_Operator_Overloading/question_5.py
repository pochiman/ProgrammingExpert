##### Vector Class #####

# Write a Vector class that implements the following dunder methods.

##### __init__(self, a, b) initializes the vector by storing the components a and b.

##### __eq__(self, vector) returns True if the current vector and the vector parameter are equal.

##### __repr__(self) returns the formal string representation of the vector.

##### __add__(self, vector) creates and returns a new Vector object that has components equal to the 
##### sum of the components in the current vector and the vector represented by the vector parameter.

##### __sub__(self, vector) creates and returns a new Vector object that has components equal to the 
##### difference of the components in the current vector and the vector represented by the vector parameter.

##### __mul__(self, vector) returns the dot product of the current vector and the vector represented by the vector parameter.
##### The dot product of two vectors is equal to the sum of the multiplication of their individual components.

# See below for the expected output of a program that uses the Vector class.

# >>> v1 = Vector(3, 4)
# >>> v2 = Vector(-4, 5)
# >>> v1 == v2
# False
# >>> v1 == Vector(3, 4)
# True
# >>> repr(v1)
# Vector(3, 4)
# >>> v3 = v1 + v2
# >>> repr(v3)
# Vector(-1, 9)
# >>> v4 = v2 - v1
# >>> repr(v4)
# Vector(-7, 1)
# >>> v5 = Vector(4, 0)
# >>> v1 * v2
# 8

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b
        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)

    def __mul__(self, vector):
        return self.a * vector.a + self.b * vector.b
##### Rectangle Class #####

# Add the following methods to the Rectangle class:

##### change_position(...): this method should accept two parameters, one for the x position and the other for the y position.
##### It should set the corresponding instance attributes such that they are equal to the arguments passed to the method.

##### get_position(...): this method should return the position of the rectangle as a tuple in the form (x, y).

##### get_area(...): this method should return the area of the rectangle.  It should calculate the area by using the appropriate 
##### instance attributes.

# You do not need to make any instances of the class once you have added the methods.
# See below for the expected output of a program that uses the Rectangle class.

# >>> rect = Rectangle(10, -5, 5, 3)
# >>> pos = rect.get_position()
# >>> print(pos)
# (10, -5)
# >>> rect.change_position(3, 4)
# >>> pos rect.get_position()
# >>> print(pos)
# (3, 4)
# >>> area = rect.get_area()
# >>> print(area)
# 15

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_area(self):
        return self.width * self.height
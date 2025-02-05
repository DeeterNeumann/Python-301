# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.


import math

class Rectangle:
    """Models a rectangale"""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rec_area(self):
        area = self.length * self.width
        self.area = area
        return f"The rectangle with a length of {self.length} and width of {self.width} has an area of {self.area}."
    
    def perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return f"The rectangle with a length of {self.length} and width of {self.width} has a perimeter of {perimeter}."

    # def __str__(self):


class Circle:
    """Models a circle"""

    def __init__(self, radius):
        self.radius = radius
    
    def cir_area(self):
        area = (math.pi * (self.radius ** 2))
        self.area = area
        return f"The circle with a radius of {self.radius} has an area of {self.area}."
    
    def circumference(self):
        circumference = (2 * math.pi * self.radius)
        return f"The circle with a radius of {self.radius} has a circumference of {circumference}."

r = Rectangle(4, 2)

c = Circle(4)

print(r.rec_area())
print(r.perimeter())

print(c.cir_area())
print(c.circumference())
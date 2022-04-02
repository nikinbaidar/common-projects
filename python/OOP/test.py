from os import system
from math import pi

system("clear")

class GeometricShapes:
    pass

class square(GeometricShapes):

    def __init__(self,length):
        self.length = length

    @property
    def area(self):
        return self.length*self.length

class rectangle(GeometricShapes):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    @property
    def area(self):
        return 2*(self.length + self.breadth)

class circle(GeometricShapes):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return pi*self.radius*self.radius

def area(shape):
    return shape.area

shape1 = square(5)
shape2 = rectangle(3,4)
shape3 = circle(1)

print(area(shape1))
print(area(shape2))
print(area(shape3))

# print(shape1.area())
# print(shape2.area())
# print(shape3.area())


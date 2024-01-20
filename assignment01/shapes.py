import math

class Shape(object):

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return self.name


def describe_shape(shape):
    print('The area of a %s is %s.' % (shape.get_name(), shape.get_area()))
    print('The perimeter of a %s is %s.' % (shape.get_name(), shape.get_perimeter()))


# Your code below

class Triangle(l1, l2, l3):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def get_area(l1, l2, l3):
        l4 = 0.5 * l2
        return l4 * l1 * l3

    def get_perimeter(l1, l2, l3):
        return l1 + l2 + l3

triangle = Triangle(2, 4, 6)
print(triangle.get_area)

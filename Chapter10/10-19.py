import math

class Circle:
    def __init__(self, radius = 10):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi*self.__radius**2

    def get_circumference(self):
        return 2*math.pi*self.__radius

c1 = Circle(7)
print('넓이:', c1.get_area())
print('둘레:', c1.get_circumference())
c1.set_radius(10)
print('넓이:', c1.get_area())
print('둘레:', c1.get_circumference())
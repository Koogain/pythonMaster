class Figure:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

class Circle(Figure):
    def __init__(self, radius = 10):
        area = 3.14 * radius ** 2
        perimeter = 2 * 3.14 * radius
        super().__init__(area, perimeter)
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius
        self.area = 3.14 * radius ** 2
        self.perimeter = 2 * 3.14 * radius

    def get_radius(self):
        return self.radius

class Rectangle(Figure):
    def __init__(self, width = 10, height = 10):
        area = width * height
        perimeter = 2 * width + 2 * height
        super().__init__(area, perimeter)
        self.width = width
        self.height =height

    def set_width(self, width):
        self.width = width
        self.area = width * self.height
        self.perimeter = 2 * width + 2 * self.height

    def set_height(self, height):
        self.height = height
        self.area = self.width * height
        self.perimeter = 2 * self.width + 2 * height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

f1 = Circle(7)
print(f1.get_area(), f1.get_perimeter())
f1.set_radius(10)
print(f1.get_area(), f1.get_perimeter())

f2 = Rectangle(5, 4)
print(f2.get_area(), f2.get_perimeter())
f2.set_width(7)
print(f2.get_area(), f2.get_perimeter())
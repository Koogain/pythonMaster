class Student:
    def __init__(self, name, math, computer):
        self.__name = name
        self.__math = math
        self.__computer = computer

    def get_name(self):
        return self.__name

    def get_average(self):
        return (self.__math + self.__computer)/2

    def set_math(self, math):
        self.__math = math

    def set_computer(self, computer):
        self.__computer = computer

s1 = Student('hanbit', 95, 89)
print(s1.get_name(), s1.get_average())
s1.set_computer(97)
print(s1.get_name(), s1.get_average())
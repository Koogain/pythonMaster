class Calculator:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def set_data(self, a, b):
        self.a = a
        self.b = b

cal = Calculator(10, 5)
print(cal.sub())
print(cal.mul())
cal.set_data(9, 3)
print(cal.add())
print(cal.div())
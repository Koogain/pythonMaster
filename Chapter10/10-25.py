class Student:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

    def set_computer(self, computer):
        self.computer = computer

    def get_name(self):
        return self.name


class Science(Student):
    def __init__(self, name, computer, science):
        super().__init__(name, computer)
        self.science = science

    def set_science(self, science):
        self.science = science

    def get_average(self):
        return (self.science + self.computer) / 2


st1 = Science('gain', 100, 100)

print(st1.get_average())
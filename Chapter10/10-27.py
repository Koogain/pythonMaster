class Student:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

    def set_computer(self, computer):
        self.computer = computer

    def get_name(self):
        return self.name


class Liberalarts(Student):
    def __init__(self, name, computer, social):
        super().__init__(name, computer)
        self.social = social

    def set_social(self, social):
        self.social = social

    def get_average(self):
        return (self.social + self.computer) / 2

st2 = Liberalarts('haeun', 99, 99)
print(st2.get_average())
st2.set_social(99)
print(st2.get_name(), ':', st2.get_average())
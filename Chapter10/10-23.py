class Student:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

    def set_computer(self, computer):
        self.computer = computer

    def get_name(self):
        return self.name

class Leberarts(Student):
    def __init__(self, name, computer, social):
        super().__init__(name, computer)
        self.social = social

    def set_social(self, social):
        self.social = social

    def get_average(self):
        return (self.social + self.computer) / 2
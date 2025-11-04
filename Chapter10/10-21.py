class Student:
    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

    def set_computer(self, computer):
        self.computer = computer

    def get_name(self):
        return self.name
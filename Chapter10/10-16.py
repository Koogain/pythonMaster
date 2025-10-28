class Account:
    def __init__(self, amount = 0):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

a1 = Account(50)
a1.balance = 30
print(a1.balance)
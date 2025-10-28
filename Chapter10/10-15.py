class Account:
    def __init__(self, amount = 0):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

a1 =Account(50)
print(a1.deposit(70))

a2 = Account()
print(a2.deposit(100))
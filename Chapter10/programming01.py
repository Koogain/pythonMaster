class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a1 = Account()
print(a1.deposit(100))
print(a1.withdraw(30))

a2 = Account()
print(a2.deposit(70))
print(a2.withdraw(20))

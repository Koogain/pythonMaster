class Account:
    def __init__(self, amount = 0):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

a1 = Account(50)
print(a1.__balance)
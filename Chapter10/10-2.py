balance1 = 0
balance2 = 0

def deposit1(amount):
    global balance1
    balance1 += amount
    return balance1

def deposit2(amount):
    global balance2
    balance2 += amount
    return balance2

def withdraw1(amount):
    global  balance1
    balance1 -= amount
    return balance1

def withdraw2(amount):
    global  balance2
    balance2 -= amount
    return balance2

print(deposit1(100))
print(withdraw1(30))

print(deposit2(100))
print(withdraw2(30))
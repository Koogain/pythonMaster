import random
from math import remainder

a = random.randint(1, 100)
b = random.randint(1, 100)      #code 3-16
answer = int(input(f'{a} + {b} = '))
if answer == a + b:
    print('맞혔습니다.')
else:
    print('틀렸습니다.')

a = random.randint(1, 100)
b = random.randint(1, 100)
answer = int(input(f'{a} + {b} = '))
if answer == a + b:
    print('맞혔습니다.')
else:
    print('틀렸습니다.')
print()

import random

def rand_add():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = int(input(f'{a} + {b} = '))    #code 3-17
    if answer == a + b:
        print('맞혔습니다.')
    else:
        print('틀렸습니다.')

rand_add()
rand_add()
print()

def func():
    print('함수입니다.')     #code 3-18

print('함수 호출 전입니다.')
func()
print('함수 호출 후입니다.')
print()

def add(x, y):
    print(x + y)

a = int(input('정수: '))      #code 3-19
b = int(input('정수: '))
add(a, b)
print()

def add(x, y):
    return x + y

a = int(input('정수: '))      #code 3-20
b = int(input('정수: '))
print(add(a, b))
print()

import random

def bigsmall(x, y):
 if x > y:
    return x, y
 else:
    return y, x

a = random.randint(1, 100)      #code 3-21
b = random.randint(1, 100)
a, b = bigsmall(a, b)
print(a, b)
print()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

a = int(input('정수: '))      #code 3-22
b = int(input('정수: '))
print(f'{a} + {b} = {add(a, b)}')
print(f'{a} - {b} = {sub(a, b)}')
print(f'{a} * {b} = {mul(a, b)}')
print(f'{a} / {b} = {div(a, b)}')
print()

def div(x, y):
    return x // y, x % y        #code 3-23

a = int(input('정수: '))
b = int(input('정수: '))
quotient, remainder = div(a, b)
print(f'{a}를 {b}로 나눈 몫은 {quotient}이고 나머지는 {remainder}')
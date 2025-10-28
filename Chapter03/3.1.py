a, b, c = 10, 20, 20
print(f'{a}=={b}: {a==b}')
print(f'{a}!={b}: {a!=b}')
print(f'{a}>{b}: {a>b}')
print(f'{b}<{c}: {b<c}')    #code 3-1
print(f'{a}>={b}: {a>=b}')
print(f'{b}<={c}: {b<=c}')
print()

import random
x = random.randint(1,5)       #code 3-2
answer = int(input("선택한 수를 맞혀보세요(1~5): "))
print(x == answer, '선택한 수는', x)
print()

import random

i = random.randint(10,50)
j = random.randint(2, 9)
my_quotient = int(input(f'{i}를 {j}로 나눈 몫: '))   #code 3-3
print(a//b == my_quotient)
my_remainder = int(input(f'{i}를 {j}로 나눈 나머지: '))
print(a%b == my_remainder)
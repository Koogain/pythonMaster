import random
a = random.randint(1, 100)
b = random.randint(1, 100)  #code 3-4
if a < b:
    a, b = b, a
print(a, b)
print()

height1 = int(input('키: '))
height2 = int(input('키: '))     #code 3-5
if height1 > height2:
    print('키 차이: ', height1 - height2)
else:
    print('키 차이: ', height2 - height1)
print()

fee = 5000
age = int(input('나이: '))
if age < 8:
    print('입장료: ', fee * 0.7)   #code 3-6
elif age < 60:
    print('입장료: ', fee)
else:
    print('입장료: ', fee * 0.8)
print()

price = int(input('가격: '))  #code 3-7
if price >= 10000:
    price *= 0.95
print('판매가: ', price)
print()

num = int(input('정수: '))    #code 3-8
if num % 2 == 0:
    print(f'{num}: 짝수')
else:
    print(f'{num}: 홀수')
print()

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)    #code 3-9
if dice1 > dice2:
    print(f'주사위1 승')
elif dice1 < dice2:
    print(f'주사위2 승')
else:
    print(f'무승부')
print()

try1 = int(input('첫 번째 기록(초): '))
try2 = int(input('두 번째 기록(초): '))   #code 3-10
try3 = int(input('세 번째 기록(초): '))

if try1 < try2:
 if try1 < try3:
    print('선수 기록: ', try1)
 else:
    print('선수 기록: ', try3)
else:
   if try2 < try3:
    print('선수 기록: ', try2)
   else:
       print('선수 기록: ', try3)
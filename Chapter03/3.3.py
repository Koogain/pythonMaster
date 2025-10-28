delivery_fee = 2000
level = input('회원 등급(우수 또는 일반): ')
price = int(input('구매액: '))

if level == '우수':
    print('결제 금액:', price)  #code 3-11
elif price >= 20000:
    print('결제 금액:', price)
else:
    print('결제 금액:', price + delivery_fee)
print()

delivery_fee = 2000
level = input('회원 등급(우수 또는 일반): ')  #code 3-12
price = int(input('구매액: '))

if level == '우수' or price >= 20000:
    print('결제금액: ', price)
else:
    print('결제금액: ', price + delivery_fee)
print()

a = int(input('정수: '))
if a % 3 == 0 and a % 5 == 0:   #code 3-13
    print('3과 5의 배수')
else:
    print('3과 5의 배수 아님')
print()

year = int(input('연도: '))   #code 3-14
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('윤년')
else:
    print('평년')
print()

import random   #code 3-15

user = input('가위, 바위, 보: ')
com_rand = random.randint(1,3)  #code 3-16
if com_rand == 1:
    computer = '가위'
elif com_rand == 2:
    computer = '바위'
else:
    computer = '보'
print(f'나:{user} 컴퓨터:{computer}')

if user == computer:
    print('무승부')
elif user == '가위' and computer == '보':
    print('승')
elif user == '바위' and computer == '가위':
    print('승')
elif user == '보' and computer == '바위':
    print('승')
else:
    print('패')
print()
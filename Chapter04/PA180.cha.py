import random

answer = random.randint(1,2)
times = 0

while True:
    user = input('선택(좌 또는 우): ')
    if answer == 1:
        computer = '좌'
    else:
        computer = '우'
    times += 1
    if user == computer:
        print(f'방어 실패(컴퓨터:{computer}, 사용자:{user}')
        break
    elif user != computer:
        print(f'방어 성공(컴퓨터:{computer}, 사용자:{user}')
    else:
        print('잘못된 공격입니다.')
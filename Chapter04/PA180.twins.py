import random
print('1부터 100까지의 수 하나를 정했습니다.')
print('이 숫자를  맞혀보세요.')

answer = random.randint(1, 100)
times = 0

while True:
    user = int(input('사용자 선택: '))
    times += 1
    if user == answer:
        break
    elif user < answer:
        print(f'{user}보다 큽니다.')
    else:
        print(f'{user}보다 작습니다.')

print(f'정답입니다! {times}회 만에 맞혔습니다.')
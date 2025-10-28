quiz = ['자를 의미하는 동물은? ', '축를 의미하는 동물은? ', '인를 의미하는 동물은? ',
        '묘를 의미하는 동물은? ', '진를 의미하는 동물은? ', '사를 의미하는 동물은? ',
        '오를 의미하는 동물은? ', '미를 의미하는 동물은? ', '신를 의미하는 동물은? ',
        '유를 의미하는 동물은? ', '술를 의미하는 동물은? ', '해를 의미하는 동물은? ']

answer = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지']
quiz_num = int(input('풀어보실 문항 수를 선택해 주세요: '))
idx = quiz_num

import random

times = 0
right_time = 0
i = 1
while i <= quiz_num:
    print(random.choices(quiz, k=1))
    user = input('정답을 작성하시오: ')
    i += 1
    for idx, a in enumerate(quiz):
        times += 1
        if user in answer:
            print('정답입니다.')
            quiz.pop(idx)
            right_time += 1
            break
        else:
            print('틀리셨습니다.')
            break

print(f'풀어본 문항 수: {times}회, 맞힌 문항 수: {right_time}회')
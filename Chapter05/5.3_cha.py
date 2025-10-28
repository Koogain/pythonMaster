hanza_name = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

animal_name = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지']

while True:
    answer = input('한자동물이름, 한글 동물 이름 혹은 종료: ')
    if answer == '종료':
        print('종료합니다.')
        break;
    elif answer in hanza_name:
        idx = hanza_name.index(answer)
        print('동물 번호 ', idx + 1, '동물 이름: ', animal_name[idx])
    elif answer in animal_name:
        idx = animal_name.index(answer)
        print('한자 번호: ', idx + 1, '한자: ', hanza_name[idx])
    else:
        print('잘못 입력했습니다.')

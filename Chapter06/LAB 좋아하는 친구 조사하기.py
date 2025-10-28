lst = []
i = 1
while True:
    s = input(f'{i}번 학생을 좋아하는 친구(,로 구분) 또는 종료: ')
    if s == '종료':
        break
    lst.extend(s.split(','))
    i += 1
print(lst)
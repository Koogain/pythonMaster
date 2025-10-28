langs = {'python': 0, 'c': 0, 'java': 0, 'javascript': 0}

while True:
    s = input('선호하는 언어(python,c,java,javascript)또는 초기화, 종료: ')
    if s == '종료':
        print('종료합니다.')
        break
    elif s == '초기화':
        print('초기화합니다.')
        langs.clear()
        langs = {'python': 0, 'c': 0, 'java': 0, 'javascript': 0}
    elif s in langs:
        langs[s] += 1
    else:
        print(f'{s}는 등록되지 않은 언어입니다.')

for key, value in langs.items():
    print(key, value)
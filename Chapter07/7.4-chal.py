langs = {}

while True:
    s = input('좋아하는 메뉴 또는 초기화, 종료: ')
    if s == '종료':
        print('종료합니다.')
        break
    elif s == '초기화':
        print('초기화합니다.')
        langs.clear()
    elif s in langs:
        langs[s] += 1
    else:
        langs[s] = 1

for key, value in langs.items():
    print(key, value)
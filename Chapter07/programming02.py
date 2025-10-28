hanza_name = {'자':'쥐', '축':'소', '인':'호랑이', '묘':'토끼', '진':'용',
                '사':'뱀', '오':'말', '미':'양', '신':'원숭이', '유':'닭', '술':'개', '해':'돼지'}

while True:
    s = input('한자 동물 이름 또는 종료: ')
    if s == '종료':
        print('종료합니다.')
        break
    elif s in hanza_name:
         print(hanza_name[s])
    else:
        print('잘못 입력했습니다.')

for key,value in hanza_name.items():
    print(key, value)
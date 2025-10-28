do_name = ['경기도', '충청북도', '충청남도', '경상북도', '경상남도', '전라북도', '전라남도', '강원특별자치도', '제주특별자치도']

dochung_sojaejee = ['수원', '청주', '홍성', '안동', '창원', '전주', '무안', '춘천', '제주']

while True:
    answer = input('도, 도청 소재지 혹은 종료: ')
    if answer == '종료':
        print('종료합니다.')
        break;
    elif answer in do_name:
        idx = do_name.index(answer)
        print('도청 소재지: ', dochung_sojaejee[idx])
    elif answer in dochung_sojaejee:
        idx = dochung_sojaejee.index(answer)
        print('도: ', do_name[idx])
    else:
        print('잘못 입력했습니다.')
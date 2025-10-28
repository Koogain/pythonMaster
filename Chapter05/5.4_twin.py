element_name = ['수소', '헬륨', '리튬', '베릴륨', '붕소', '탄소', '질소', '산소', '플루오린', '네온',
'나트륨', '마그네슘', '알루미늄', '실리콘', '인', '황', '염소', '아르곤', '칼륨', '칼슘',
'스칸듐', '타이타늄', '바나듐', '크로뮴', '망가니즈', '철', '코발트', '니켈', '구리', '아연',
'갈륨', '저마늄', '비소', '셀레늄', '브로민', '크립톤', '루비듐', '스트론튬', '이터븀', '지르코늄',
'나이오븀', '몰리브덴', '테크네튬', '루테늄', '로듐', '팔라듐', '은', '백금', '금', '수은',
'탄탈럼', '볼프람', '레늄', '흑연', '로렌슘', '모나늄', '니오븀', '크리프리즘']

element_symbol = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Pt', 'Au', 'Hg',
'Ta', 'W', 'Re', 'Ga', 'Lr', 'Mn', 'Nb', 'Cr']

while True:
    answer = input('원소 기호, 원소 이름, 종료: ')
    if answer == '종료':
        print('종료합니다.')
        break;
    elif answer in element_symbol:
        idx = element_symbol.index(answer)
        print('원자 번호: ', idx + 1, '원소 이름: ', element_name[idx])
    elif answer in element_name:
        idx = element_name.index(answer)
        print('원자 번호: ', idx + 1, '원소 기호: ', element_symbol[idx])
    else:
        print('잘못 입력했습니다.')
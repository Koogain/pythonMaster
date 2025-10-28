words = {}

def registration():
    regi_animal = input('등록할 영어 단어: ')
    regi_mean = input('등록한 단어의 뜻: ')
    if regi_animal in words:
        print('등록된 단어입니다.')
    else:
        words[regi_animal] = regi_mean

def quiz():
    for regi_animal, regi_mean in words.items():
        ans = input(regi_animal+'뜻은? ')
        if ans == regi_mean:
            print('맞았습니다.')
        else:
            print('틀렸습니다.')

while True:
    sel = int(input('1.등록 2.퀴즈 3.종료: '))
    if sel == 3:
        print('종료합니다.')
        break
    elif sel == 1:
        registration()
    elif sel == 2:
        quiz()
    else:
        print('잘못 입력하셨습니다.')
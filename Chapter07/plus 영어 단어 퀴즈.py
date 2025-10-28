import googletrans

translator = googletrans.Translator()

words = {}

def registration():
    s = input('등록할 단어: ')
    if s in words:
        print('등록된 단어입니다.')
    else:
        words[s] = translator.translate(s, dest='en').text

def quiz():
    for key, value in words.items():
        ans = input(key+'영어 이름은? ')
        if ans == value:
            print('맞았습니다.')
        else:
            print('틀렸습니다.')

while True:
    sel = int(input('1.등록 2.퀴즈 3.종료: '))
    if sel==3:
        print('종료합니다')
        break
    elif sel == 2:
        quiz()
    elif sel == 1:
        registration()
    else:
        print('잘못 입력했습니다.')

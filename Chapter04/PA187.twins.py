#!pip install googletrans==4.0.0-rc1
import googletrans

translator = googletrans.Translator()
while True:
    lang = input('도착어 선택(영어, 일본어, 독일어, 프랑스어, 종료: ')
    if lang == '종료':
        print('종료합니다.')
        break
    elif lang == '영어':
        lang = 'en'
    elif lang == '일본어':
        lang = 'jp'
    elif lang == '독일어':
        lang = 'de'
    elif lang == '프랑스어':
        lang = 'fr'
    else:
        print('잘못 입력했습니다.')
        continue
    scr = input('번역할 내용을 입력하세요: ')
    dest = translator.translate(scr, dest=lang)
    print(dest.text)
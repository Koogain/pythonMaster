s = input('문자열: ')

if len(s) >= 4 and s.find('zzz') == -1:
    print('pass')

else:
    print('fail')
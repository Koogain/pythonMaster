s1 = input('문자열: ')
s2 = ''

for i in range(len(s1)-1,-1,-1):
    s2 = s2 + s1[i]

if s1 == s2:
    print('회문입니다.')

else:
    print('회문이 아닙니다.')
# 알파벳 문자열
alphabet_str = "abcdefghijklmnopqrstuvwxyz"

# 모스 부호 리스트
morse_code_list = [
    ".-",    # a
    "-...",  # b
    "-.-.",  # c
    "-..",   # d
    ".",     # e
    "..-.",  # f
    "--.",   # g
    "....",  # h
    "..",    # i
    ".---",  # j
    "-.-",   # k
    ".-..",  # l
    "--",    # m
    "-.",    # n
    "---",   # o
    ".--.",  # p
    "--.-",  # q
    ".-.",   # r
    "...",   # s
    "-",     # t
    "..-",   # u
    "...-",  # v
    ".--",   # w
    "-..-",  # x
    "-.--",  # y
    "--.."   # z
]
while True:
    s = input('알파벳 문자열, 모스부호, 종료: ')

    if s == '종료':
        break
    else:
        if s in alphabet_str:
            for i in range(len(s)):
                if s[i] in alphabet_str:
                    print(morse_code_list[alphabet_str.index(s[i])], end='')
        elif s in morse_code_list:
            for i in range(len(s)):
                if s[i] in morse_code_list:
                    print(alphabet_str[morse_code_list.index(s[i])], end='')
        else:
            print('잘못된 문자입니다.')
    print()
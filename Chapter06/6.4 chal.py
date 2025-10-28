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
    s = input('알파벳 문자열: ')

    for i in range(len(s)):
        if s[i] in alphabet_str:
            print(morse_code_list[alphabet_str.index(s[i])], end='')

    print()
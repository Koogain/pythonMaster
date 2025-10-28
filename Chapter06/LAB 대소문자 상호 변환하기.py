while True:
    input_str1 = input('문자열을 입력하시오: ')
    str2 = ''
    for ch in input_str1:
        if ch.islower():
            str2 += ch.upper()
        elif ch.isupper():
            str2 += ch.islower()
        else:
            str2 += ch
    print(str2)

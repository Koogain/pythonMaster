s = input('문자열: ')

count_alpha = 0
count_digit = 0
count3 = 0

for i in s:
    if i.isalpha():
        count_alpha += 1

    elif i.isdigit():
        count_digit += 1

    else:
        count3 += 1

print(f'영문자: {count_alpha} 숫자: {count_digit} 기타문자: {count3}')


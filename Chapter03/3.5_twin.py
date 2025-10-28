kind = input('온도 종류(섭씨 또는 화씨): ')
temp = int(input(kind +' 온도: '))

if kind == '화씨':
    print(f'섭씨 온도 {(temp - 32) * 5 / 9}')
else:
    print(f'화씨 온도 {temp * 9 / 5 + 32}')
print()
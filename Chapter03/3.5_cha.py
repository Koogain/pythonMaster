kind = input('넓이 단위(제곱미터 또는 평: ')
area = int(input(kind +' 넓이: '))

if kind == '제곱미터':
    print(f'넓이: {area}')
else:
    print(f'평 넓이 {area * 0.3025}')
print()
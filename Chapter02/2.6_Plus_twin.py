nomal_price = 1300
teenager_price = 1000
child_price = 450

sum = 0
namal_num = int(input('일반 인원: '))
sum += namal_num * nomal_price

teenager_num = int(input('청소년 인원: '))
sum += teenager_num * teenager_price

child_num = int(input('어린이 인원: '))
sum += child_num * child_price

print('전체 요금:', sum)

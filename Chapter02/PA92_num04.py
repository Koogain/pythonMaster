normal_price = 5000
old_price = normal_price * 0.5
child_price = normal_price * 0.4

sum = 0

child_num = int(input('8세 미만 인원 수: '))
sum += child_num * child_price

normal_num = int(input('8세 이상 60세 미만 인원 수: '))
sum += normal_num * normal_price

old_num = int(input('60세 이상 인원 수: '))
sum += old_num * old_price


print('전체 요금:', sum)
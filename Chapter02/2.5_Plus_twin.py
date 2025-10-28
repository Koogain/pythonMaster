second = int(input('분 단위 시간: '))
day = min // 1440
min = min % 1440
hour = min // 60
min = min % 60
print(f'{day}일 {hour}시간 {min}분')
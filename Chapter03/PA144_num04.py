kilogram = int(input('몸무게? '))
height = float(input('키? '))
height *= 0.01
BMI = kilogram / (height * height)

if BMI < 18.5:
    print('저체중입니다.')
elif 18.5 <= BMI < 23:
    print('정상입니다.')
elif 23 <= BMI < 25:
    print('과체중입니다.')
elif 25 <= BMI < 30:
    print('1단계 비만입니다.')
elif 30 <= BMI < 35:
    print('2단계 비만입니다.')
else:
    print('고도비만입니다.')
import math

def square():
    width = int(input('사각형의 가로: '))
    height = int(input('사각형의 가로: '))
    return width * height

def triagle():
    base = int(input('삼각형의 밑변: '))
    height = int(input('삼각형의 높이: '))
    return base * height / 2

def circle():
    radius = int(input('원의 반지름: '))
    return math.pi * radius ** 2

shape_type1 = input('도형의 종류(사각형, 삼각형, 원)')
if shape_type1 == '사각형':
 area1 = square()
elif shape_type1 == '삼각형':
 area1 = triagle()
else:
 area3 = circle()

 shape_type2 = input('도형의 종류(사각형, 삼각형, 원)')
 if shape_type2 == '사각형':
     area2 = square()
 elif shape_type2 == '삼각형':
     area2 = triagle()
 else:
     area2 = circle()

if area1 > area2:
    print(f',도형1(넓이:{area1})이 도형2(넓이:{area2})보다 {area1 - area2}만큼 넓습니다.')
elif area1 <area2:
    print(f',도형2(넓이:{area2})이 도형1(넓이:{area1})보다 {area2 - area1}만큼 넓습니다.')
else:
    print(f'두 도형의 넓이는 {area1}로 같습니다.')
import random

names = []
num = int(input('학생 수: '))

for i in range(num):
    names.append(input('학생 이름: '))
print(random.sample(names,2))
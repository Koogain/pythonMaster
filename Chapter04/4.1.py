import random

print(random.randint(1,100))
print(random.randint(1,100))    #4-1 code
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print()

for i in range(5):
    print(random.randint(1,100))    #4-2 code
print()

for a in range(3):
    print('안녕')         #4-3 code
print()

for a in range(2, 5):       #4-4 code
    print(a)
print()

for a in range(10, 1, -3):      #4-5 code
    print(a)
print()

sum = 1+2+3+4+5         #4-6 code
print(sum)
print()

sum1 = 0
sum1 += 1
sum1 += 2       #4-7 code
sum1 += 3
sum1 += 4
sum1 += 5
print(sum1)
print()

sum2 = 0
for a in range(1, 6):   #4-8 code
    sum2 += a
print(sum2)
print()

num = int(input('정수: '))
for a in range(1, num+1):       #4-9 code
    if num%a == 0:
        print(a, end=' ')
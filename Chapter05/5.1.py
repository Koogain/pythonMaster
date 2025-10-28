cubes = []                      #code 5-1
for x in range(1, 10):
    cubes.append(x**3)
print(cubes)

sequence = []                                 #code 5-2
for x in range(1, 101):
    if x % 7 == 0:
        sequence.append(x)
print(sequence)

score = [71, 80, 60, 90, 65]                          #code 5-3
result = []

for a in score:
    if a>= 70:
        result.append('합격')
    else:
        result.append('불합격')
print(result)

score1 = [71, 80, 60, 90, 65]
result1 = ['합격' if a >= 70 else '불합격' for a in score1]      #code 5-4
print(result1)
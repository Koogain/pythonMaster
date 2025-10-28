menus5  = ['자장면', '짬뽕', '볶음밥']      #code 5-5
for i in range(3):
    print(menus5[i])

menus6  = ['자장면', '짬뽕', '볶음밥']      #code 5-6
for i in range(len(menus5)):
    print(menus6[i])

menus7 = ['자장면', '짬뽕', '볶음밥']       #code 5-7
for a in menus7:
    print(a)

menus8 = ['자장면', '짬뽕', '볶음밥']       #code 5-8
for i, a in enumerate(menus8):
    print(i,a)

pl = []                 #code 5-9
pl.append('파이썬')
pl.append('C')
print(pl)

pl = ['파이썬', '자바']              #code 5-10
pl.insert(1, 'C')
print(pl)

pl = ['파이썬', 'C']                   #code 5-11
pl.extend(['C++', '자바'])
print(pl)

pets = ['dog', 'cat', 'hamster', 'hedgehog', 'parrot', 'lizard']        #code 5-12
select1 = pets.pop(3)
print(select1)

pets = ['dog', 'cat', 'hamster', 'hedgehog', 'parrot', 'lizard']        #code 5-13
del pets[3],pets[-1]
print(pets)

pets = ['dog', 'cat', 'hamster', 'hedgehog', 'parrot', 'lizard']        #code 5-14
pets.remove('hamster')
print(pets)

pets = ['dog', 'cat', 'hamster', 'hedgehog', 'parrot', 'lizard']        #code 5-15
pets.clear()
print(pets)

nations = ['한국', '미국', '영국', '일본']          #code 5-16
nations.reverse()
print(nations)

nations = ['한국', '미국', '영국', '일본']          #code 5-17
nations.sort()
print(nations)
nations.sort(reverse=True)
print(nations)

months = ['January', 'February', 'March', 'April', 'May', 'June',           #code 5-18
         'July', 'August', 'September', 'October', 'November', 'December']
answer = input('월(영어): ')

if answer in months:
    print(months.index(answer)+1)
else:
    print('잘못 입력했습니다.')

import random               #code 5-19

colors = ['ivory', 'lavender', 'lightcyan', 'lightyellow', 'palegreen']
print(random.choice(colors))
print(random.sample(colors, 3))
print(random.choices(colors, k=3))

import random           #code 5-20

colors = ['ivory', 'lavender', 'lightcyan', 'lightyellow', 'palegreen']
random.shuffle(colors)
print(colors[:3])

scores = [85, 95, 70, 75, 99, 93, 88]           #code 5-21

print('최댓값: ', max(scores))
print('최솟값: ', min(scores))
print('합: ', sum(scores))
print('평균: ', sum(scores)/len(scores))

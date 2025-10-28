a = int(input('정수: '))
b = int(input('정수: '))
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')
print()
#code 2-27

ave = 70 + 80 + 90 /3
print(ave)
print()
#code 2-28

ave = (70+80+90)/3
print(ave)
print()
#code 2-29

male_num = int(input('남성 지원자 수: '))
female_num = int(input('여성 지원자 수: '))
total = male_num + female_num
print(f'남성 비율:{male_num/total:.2f}여성 비율:{female_num/total:.2f}')
print()
#code 2-30

cm = int(input('센티미터 단위 길이: '))
m = cm // 100
cm = cm % 100
print(f'{m}미터 {cm}센티미터')
print()
#code 2-31
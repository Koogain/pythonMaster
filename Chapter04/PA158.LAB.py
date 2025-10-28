#4-10 code
employee_num = 3
total = 0

for i in range(employee_num):
    rank = int(input('직급: '))
    basic_salary = int(input('본봉: '))
    if rank >= 2:
        bouns = basic_salary * 0.3
    else:
        salary = basic_salary + bouns
        total += salary
print('월급총액: ', total)
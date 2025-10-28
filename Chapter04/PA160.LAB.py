#4-11 code
judge_num = 5
sum = 0
max_score = 0

for i in range(judge_num):
    score = int(input(f'심사위원{i+1} 평가점수: '))
    sum += score
    if score > max_score:
        max_score = score
sum -= max_score
print('작품 평가 점수: ', sum/(judge_num-1))
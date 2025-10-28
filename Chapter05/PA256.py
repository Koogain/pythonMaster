score = [80, 90, 85, 75, 100]

while True:
    answer = int(input())
    num = int(answer)
    if num >= 1 and num <= 5:
        print(score[num + 1])


ds = [10, 20, 30, 40, 50]
for i in range(len(ds)):
    print(f'{i+1}: {ds[i]}')

dynasties = ['태조', '정종', '태종', '세종', '문종', '단종', '세조', '예종', '성종',
             '연산군', '중종', '인종', '명종', '선조', '광해군', '인조', '효종',
             '현종', '숙종', '경종', '영조', '정조', '순조', '헌종', '철종', '고종', '순종']

while True:
    answer = input('순서, 왕 이름, 종료: ')
    if answer == '종료':
        print('종료합니다.')
        break;
    elif answer.isdigit():
        num = int(answer)
        if num >= 1 and num <= 27:
            print(dynasties[num - 1])
    else:
        if answer in dynasties:
            print(dynasties.index(answer) + 1, '대 왕입니다.')
        else:
            print(answer, '이름을 가진 왕은 없습니다.')
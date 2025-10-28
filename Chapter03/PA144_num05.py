score1 = int(input('성적1: '))
score2 = int(input('성적2: '))
score3 = int(input('성적3: '))

average = (score1 + score2 + score3) / 3

if 70 <= average:
    print('합격')
else:
    print('불합격')
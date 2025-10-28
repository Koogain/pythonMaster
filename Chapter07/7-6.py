capitals = {'대한민국':'서울', '미국':'워싱턴', '일본':'도쿄'}
nation = input('국가 이름: ')
if nation in capitals:
    print(capitals[nation])
else:
    print(f'{nation}은 등록되지 않았습니다.')
americano_prince = 2000
latte_price = 3000
greentee_price = 2500
juice_price = 2800

sum = 0
americano_num = int(input('아메리카노 주문 수: '))
sum += americano_num * americano_prince

latte_num = int(input('라떼 주문 수: '))
sum += latte_num * latte_price

greentee_num = int(input('녹차 주문 수: '))
sum += greentee_num * greentee_price

juice_num = int(input('주스 주문 수: '))
sum += juice_num * juice_price

print('주문 금액:', sum)
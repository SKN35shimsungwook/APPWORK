# 원화 금액은 정수로 계산하여 부동소수점 오차를 피한다.
price = 35000
quantity = 2
discount_percent = 10
# 먼저 주문 금액을 계산한다.
subtotal = price * quantity
# // 연산자로 원 미만 금액을 버린다.
discount = subtotal * discount_percent // 100
# f-string의 :, 서식으로 천 단위 구분 기호를 표시한다.
print(f"결제 금액: {subtotal - discount:,}원")

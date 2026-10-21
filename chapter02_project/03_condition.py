# 주문 수량과 재고를 비교하여 주문 가능 여부를 결정한다.
stock = 5
quantity = 3
# 잘못된 수량을 가장 먼저 검사한다.
if quantity <= 0:
    print("수량 오류")
elif quantity > stock:
    print("재고 부족")
else:
    print("주문 가능")

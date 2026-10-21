# 함수를 사용하여 할인 금액 계산 로직을 재사용한다.
def calculate_total(price: int, quantity: int, discount_percent: int = 0) -> int:
    # 가격, 수량, 할인율의 허용 범위를 검사한다.
    if price < 0 or quantity <= 0 or not 0 <= discount_percent <= 100:
        raise ValueError("입력값이 올바르지 않다.")
    # 수량을 반영한 주문 금액을 계산한다.
    subtotal = price * quantity
    # 할인액을 차감한 최종 금액을 반환한다.
    return subtotal - subtotal * discount_percent // 100

# 직접 실행했을 때만 예제 값을 출력한다.
if __name__ == "__main__":
    print(calculate_total(35000, 2, 10))

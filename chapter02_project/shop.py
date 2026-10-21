"""제2장 콘솔 쇼핑몰: 검색·주문·할인·재고 차감."""
from decimal import Decimal, InvalidOperation
# 검색과 주문에서 같은 상품 목록을 사용한다.
from catalog import PRODUCTS

def search(keyword: str) -> list[dict]:
    # 검색어 앞뒤 공백을 제거하고 대소문자 차이를 무시한다.
    term = keyword.strip().casefold()
    return [item for item in PRODUCTS if term in item["name"].casefold()]

def order(product_id: int, quantity: int, discount_rate: str = "0") -> dict:
    # 상품 ID에 해당하는 상품을 검색한다.
    product = next((item for item in PRODUCTS if item["id"] == product_id), None)
    if product is None:
        raise ValueError("존재하지 않는 상품이다.")
    # 수량은 1 이상이어야 한다.
    if type(quantity) is not int or quantity <= 0:
        raise ValueError("수량은 1 이상의 정수여야 한다.")
    if quantity > product["stock"]:
        raise ValueError("재고가 부족하다.")
    # Decimal을 사용하여 할인율의 소수 표현을 정확하게 계산한다.
    try:
        rate = Decimal(discount_rate)
    except (InvalidOperation, TypeError, ValueError) as error:
        raise ValueError("할인율은 숫자여야 한다.") from error
    if not rate.is_finite() or not Decimal("0") <= rate <= Decimal("1"):
        raise ValueError("할인율은 0~1 사이여야 한다.")
    # 유효성 검사가 모두 끝난 뒤에만 재고를 변경한다.
    subtotal = product["price"] * quantity
    discount = int(Decimal(subtotal) * rate)
    product["stock"] -= quantity
    # 테스트하기 쉬운 딕셔너리 형태로 결과를 반환한다.
    return {"name": product["name"], "quantity": quantity, "total": subtotal - discount}

if __name__ == "__main__":
    # 검색 결과를 출력한다.
    print("검색:", [p["name"] for p in search("키보드")])
    # 키보드 두 개를 10% 할인하여 주문한다.
    result = order(1, 2, "0.10")
    print(f'주문: {result["name"]} {result["quantity"]}개 / {result["total"]:,}원')
    print("남은 재고:", PRODUCTS[0]["stock"])

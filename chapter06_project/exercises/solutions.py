# 과제 풀이: 품절 여부와 상품 필터링을 함수로 분리한다.
from shop.data import PRODUCTS

def is_available(product: dict) -> bool:
    # 재고가 1개 이상이면 구매 가능한 상품이다.
    return product["stock"] > 0

def filter_by_category(category: str) -> list[dict]:
    # 지정한 카테고리의 상품만 반환한다.
    return [item for item in PRODUCTS if item["category"] == category]

def count_available() -> int:
    # 구매 가능한 상품 수를 계산한다.
    return sum(is_available(item) for item in PRODUCTS)

if __name__ == "__main__":
    print("구매 가능 상품 수:", count_available())
    print("주변기기:", [item["name"] for item in filter_by_category("주변기기")])

# 여러 예제에서 공통으로 사용할 상품 데이터를 정의한다.
PRODUCTS = [
    {"id": 1, "name": "무선 키보드", "price": 35000, "stock": 5},
    {"id": 2, "name": "무선 마우스", "price": 18000, "stock": 8},
    {"id": 3, "name": "모니터", "price": 190000, "stock": 0},
]

def search_products(keyword: str) -> list[dict]:
    # 앞뒤 공백과 대소문자 차이를 무시한다.
    term = keyword.strip().casefold()
    # 검색어가 포함된 상품을 리스트로 반환한다.
    return [item for item in PRODUCTS if term in item["name"].casefold()]

def available_products() -> list[dict]:
    # 재고가 있는 상품만 반환한다.
    return [item for item in PRODUCTS if item["stock"] > 0]

if __name__ == "__main__":
    print([item["name"] for item in search_products("무선")])

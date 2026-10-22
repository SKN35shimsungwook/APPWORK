# 제6장에서는 데이터베이스 모델 대신 예제 상품 데이터를 사용한다.
# 제8장에서 이 데이터를 Django ORM 모델로 교체한다.
PRODUCTS = [
    {"id": 1, "name": "무선 키보드", "price": 31500, "stock": 5, "category": "주변기기"},
    {"id": 2, "name": "무선 마우스", "price": 19000, "stock": 8, "category": "주변기기"},
    {"id": 3, "name": "모니터", "price": 190000, "stock": 0, "category": "디스플레이"},
]

def get_product(product_id: int):
    # 상품 번호가 일치하는 첫 번째 상품을 반환한다.
    return next((item for item in PRODUCTS if item["id"] == product_id), None)

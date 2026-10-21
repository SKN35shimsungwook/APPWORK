# 딕셔너리 두 개를 리스트로 묶어 여러 상품을 관리한다.
products = [
    {"name": "키보드", "stock": 5},
    {"name": "마우스", "stock": 0},
]
# 반복문으로 상품을 하나씩 확인한다.
for product in products:
    # 재고가 남아 있는 상품만 출력한다.
    if product["stock"] > 0:
        print(product["name"])

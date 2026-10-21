# 과제 1: 48,000원 상품 3개를 15% 할인한 금액을 구한다.
price = 48000
quantity = 3
print("과제 1:", price * quantity * 85 // 100)
# 과제 2: 공통 상품 목록에서 재고가 있는 상품만 출력한다.
import sys
from pathlib import Path
# 하위 폴더에서 실행해도 프로젝트 루트 모듈을 찾도록 경로를 추가한다.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from catalog import available_products, search_products
print("과제 2:", [p["name"] for p in available_products()])
# 과제 3: 이름에 '무선'이 포함된 상품을 검색한다.
print("과제 3:", [p["name"] for p in search_products("무선")])
# 과제 4: 품절된 상품 주문 시 발생하는 예외를 처리한다.
from shop import order
try:
    order(3, 1)
except ValueError as error:
    print("과제 4:", error)

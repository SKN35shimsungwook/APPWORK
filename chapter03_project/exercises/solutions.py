"""실습 과제 모범 풀이: 품절 상품과 전체 재고 계산."""
import sys
from pathlib import Path

# exercises/ 폴더에서 실행해도 프로젝트 루트의 catalog 패키지를 찾도록 경로를 추가한다.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from catalog.repository import ProductRepository
from catalog.service import ProductService

def out_of_stock(service: ProductService) -> list[dict]:
    # 재고가 0인 상품만 추린다.
    return [p for p in service.list_products() if p["stock"] == 0]

def total_stock(service: ProductService) -> int:
    # 전체 상품의 재고 수량을 합산한다.
    return sum(p["stock"] for p in service.list_products())

if __name__ == "__main__":
    service = ProductService(ProductRepository("data/products.json"))
    print("품절 상품:", [p["name"] for p in out_of_stock(service)])
    print("전체 재고:", total_stock(service))

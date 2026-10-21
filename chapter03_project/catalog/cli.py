"""사용자 입력을 처리하는 CLI 계층."""
import argparse
from pathlib import Path
from catalog.exceptions import ProductError
from catalog.repository import ProductRepository
from catalog.service import ProductService

def build_parser() -> argparse.ArgumentParser:
    # 명령어와 인자를 정의한다.
    parser = argparse.ArgumentParser(description="제3장 상품 관리 프로그램")
    parser.add_argument("--data", default="data/products.json", help="JSON 저장 경로")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="상품 목록")
    search = commands.add_parser("search", help="상품 검색")
    search.add_argument("keyword", help="검색어")
    order = commands.add_parser("order", help="상품 주문")
    order.add_argument("product_id", type=int, help="상품 번호")
    order.add_argument("quantity", type=int, help="주문 수량")
    return parser

def main(argv: list[str] | None = None) -> int:
    # 명령행 인자를 해석한다.
    args = build_parser().parse_args(argv)
    service = ProductService(ProductRepository(Path(args.data)))
    try:
        if args.command == "list":
            for p in service.list_products():
                print(f'{p["id"]}. {p["name"]} | {p["price"]:,}원 | 재고 {p["stock"]}')
        elif args.command == "search":
            results = service.search(args.keyword)
            for p in results:
                print(f'{p["id"]}. {p["name"]} | {p["price"]:,}원')
            if not results:
                print("검색 결과가 없습니다.")
        elif args.command == "order":
            result = service.order(args.product_id, args.quantity)
            print(f'주문 완료: {result["name"]} {result["quantity"]}개 / {result["total"]:,}원')
            print(f'남은 재고: {result["stock"]}')
    except (ProductError, ValueError, OSError) as error:
        # 예상 가능한 오류를 사용자에게 알리고 실패 코드를 반환한다.
        print(f"오류: {error}")
        return 1
    return 0

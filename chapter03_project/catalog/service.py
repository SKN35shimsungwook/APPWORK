"""상품 조회·검색·주문을 처리하는 비즈니스 계층."""
from catalog.exceptions import InsufficientStockError, ProductNotFoundError
from catalog.repository import ProductRepository

class ProductService:
    """저장 방식과 무관하게 상품 업무 규칙을 실행한다."""

    def __init__(self, repository: ProductRepository):
        # 데이터 접근 객체를 주입받는다.
        self.repository = repository

    def list_products(self) -> list[dict]:
        # 저장소에서 상품 목록을 읽는다.
        return self.repository.load()

    def search(self, keyword: str) -> list[dict]:
        # 공백을 제거하고 대소문자를 무시한다.
        term = keyword.strip().casefold()
        # 상품명에 검색어가 포함된 상품을 반환한다.
        return [p for p in self.list_products() if term in p["name"].casefold()]

    def order(self, product_id: int, quantity: int) -> dict:
        # 주문 수량은 1 이상이어야 한다.
        if quantity <= 0:
            raise ValueError("주문 수량은 1 이상이어야 합니다.")
        products = self.repository.load()
        # 일치하는 상품 ID를 검색한다.
        product = next((p for p in products if p["id"] == product_id), None)
        if product is None:
            raise ProductNotFoundError(f"상품 {product_id}번이 없습니다.")
        if product["stock"] < quantity:
            raise InsufficientStockError("재고가 부족합니다.")
        # 재고를 차감하고 JSON 파일에 저장한다.
        product["stock"] -= quantity
        self.repository.save(products)
        # 호출자가 결과를 출력할 수 있도록 주문 정보를 반환한다.
        return {"name": product["name"], "quantity": quantity,
                "total": product["price"] * quantity, "stock": product["stock"]}

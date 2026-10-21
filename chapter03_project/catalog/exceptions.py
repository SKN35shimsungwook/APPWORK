"""상품 관리에서 사용하는 사용자 정의 예외."""

class ProductError(Exception):
    """상품 처리 실패를 표현하는 기본 예외."""

class ProductNotFoundError(ProductError):
    """상품 ID가 존재하지 않을 때 발생한다."""

class InsufficientStockError(ProductError):
    """요청한 주문 수량이 재고를 초과할 때 발생한다."""

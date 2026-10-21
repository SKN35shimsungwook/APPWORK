"""상품 업무 로직에 대한 pytest 테스트."""
import pytest
from catalog.exceptions import InsufficientStockError, ProductNotFoundError

def test_search(service):
    assert [p["name"] for p in service.search("키보드")] == ["무선 키보드"]

def test_search_ignores_spaces(service):
    assert len(service.search("  마우스  ")) == 1

def test_order_updates_stock(service):
    result = service.order(1, 2)
    assert result["total"] == 63000
    assert result["stock"] == 3
    assert service.list_products()[0]["stock"] == 3

def test_order_missing_product(service):
    with pytest.raises(ProductNotFoundError):
        service.order(999, 1)

def test_order_insufficient_stock(service):
    with pytest.raises(InsufficientStockError):
        service.order(3, 1)

def test_order_invalid_quantity(service):
    with pytest.raises(ValueError):
        service.order(1, 0)

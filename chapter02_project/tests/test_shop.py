# pytest의 assert와 raises를 사용하여 주문 기능을 검증한다.
import pytest
from catalog import PRODUCTS, available_products
from shop import order, search

def test_search():
    # 상품 이름에 검색어가 포함되면 검색된다.
    assert search("키보드")[0]["id"] == 1

def test_order_and_stock():
    # 35,000원 × 2개 × 90% = 63,000원이다.
    result = order(1, 2, "0.10")
    assert result["total"] == 63000
    assert PRODUCTS[0]["stock"] == 3

def test_invalid_quantity():
    # 0개 주문은 예외를 발생시킨다.
    with pytest.raises(ValueError, match="수량"):
        order(1, 0)

def test_out_of_stock():
    # 품절된 모니터는 주문할 수 없다.
    with pytest.raises(ValueError, match="재고"):
        order(3, 1)

def test_unknown_product():
    # 존재하지 않는 상품 ID는 예외를 발생시킨다.
    with pytest.raises(ValueError, match="존재"):
        order(99, 1)

def test_invalid_discount_rate():
    # 100%를 초과하는 할인율은 거부한다.
    with pytest.raises(ValueError, match="할인율"):
        order(1, 1, "1.2")

def test_invalid_discount_text_preserves_stock():
    # 할인율 변환 오류 시 재고가 차감되면 안 된다.
    with pytest.raises(ValueError, match="숫자"):
        order(1, 1, "abc")
    assert PRODUCTS[0]["stock"] == 5

def test_available_products():
    # 재고가 있는 상품만 목록에 포함된다.
    assert len(available_products()) == 2

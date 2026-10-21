# pytest에서 테스트별로 변경된 재고를 원래 상태로 복구한다.
from copy import deepcopy
import pytest
from catalog import PRODUCTS

@pytest.fixture(autouse=True)
def restore_products():
    # 각 테스트 시작 전에 상품 목록의 복사본을 저장한다.
    snapshot = deepcopy(PRODUCTS)
    yield
    # 테스트 종료 후 변경된 재고와 상품을 복구한다.
    PRODUCTS[:] = snapshot

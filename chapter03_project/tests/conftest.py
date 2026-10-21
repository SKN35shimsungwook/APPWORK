"""pytest 공통 fixture를 정의한다. 직접 실행하지 않는다."""
import pytest
from catalog.repository import ProductRepository
from catalog.service import ProductService

@pytest.fixture
def service(tmp_path):
    # 테스트마다 별도 임시 JSON 경로를 사용한다.
    repository = ProductRepository(tmp_path / "products.json")
    return ProductService(repository)

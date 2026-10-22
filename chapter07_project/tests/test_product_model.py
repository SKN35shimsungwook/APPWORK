# Django ORM이 MySQL에 상품을 저장하고 조회하는지 검증한다.
import pytest
from shop.models import Product


@pytest.mark.django_db
def test_create_product():
    # 테스트 DB에 상품을 생성한다.
    product = Product.objects.create(name="모니터", price=220000, stock=8)
    # 저장한 값이 데이터베이스에서 다시 조회되는지 확인한다.
    assert Product.objects.get(pk=product.pk).name == "모니터"
    assert Product.objects.count() == 1


@pytest.mark.django_db
def test_product_ordering():
    # 상품 목록은 등록 순서(id)대로 반환되어야 한다.
    Product.objects.create(name="키보드", price=65000, stock=3)
    Product.objects.create(name="마우스", price=25000, stock=4)
    assert list(Product.objects.values_list("name", flat=True)) == ["키보드", "마우스"]

# Django 테스트 클라이언트로 상품 목록 웹 화면을 검증한다.
import pytest
from django.urls import reverse
from shop.models import Product


@pytest.mark.django_db
def test_product_list_page(client):
    # 상품을 준비한 뒤 목록 화면을 요청한다.
    Product.objects.create(name="노트북", price=1200000, stock=5)
    response = client.get(reverse("product_list"))
    assert response.status_code == 200
    assert "노트북" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_empty_product_list(client):
    # 데이터가 없으면 빈 목록 안내가 표시되어야 한다.
    response = client.get(reverse("product_list"))
    assert response.status_code == 200
    assert "등록된 상품이 없습니다." in response.content.decode("utf-8")

# Django 테스트 클라이언트로 MTV 응답을 검증한다.
from django.urls import reverse

def test_product_list_status_and_template(client):
    response = client.get(reverse("shop:product_list"))
    assert response.status_code == 200
    assert "shop/product_list.html" in [t.name for t in response.templates]
    assert "무선 키보드" in response.content.decode()

def test_product_list_search(client):
    response = client.get(reverse("shop:product_list"), {"q": "마우스"})
    assert response.status_code == 200
    assert len(response.context["products"]) == 1
    assert response.context["products"][0]["name"] == "무선 마우스"

def test_product_list_no_result(client):
    response = client.get(reverse("shop:product_list"), {"q": "존재하지않음"})
    assert response.status_code == 200
    assert "검색 결과가 없습니다." in response.content.decode()

def test_product_detail(client):
    response = client.get(reverse("shop:product_detail", args=[1]))
    assert response.status_code == 200
    assert response.context["product"]["name"] == "무선 키보드"

def test_product_detail_not_found(client):
    response = client.get(reverse("shop:product_detail", args=[999]))
    assert response.status_code == 404

def test_product_list_links(client):
    response = client.get(reverse("shop:product_list"))
    assert reverse("shop:product_detail", args=[2]) in response.content.decode()

def test_static_css_link(client):
    response = client.get(reverse("shop:product_list"))
    assert "/static/shop/style.css" in response.content.decode()

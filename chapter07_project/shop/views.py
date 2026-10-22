# MySQL에 저장된 상품을 조회하여 템플릿으로 전달한다.
from django.shortcuts import render
from .models import Product


def product_list(request):
    # ORM으로 데이터베이스 상품 목록을 조회한다.
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

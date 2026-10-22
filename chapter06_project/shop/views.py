# View는 요청을 받고 템플릿에 전달할 데이터를 준비한다.
from django.http import Http404
from django.shortcuts import render
from .data import PRODUCTS, get_product

def product_list(request):
    # GET 검색어가 없으면 모든 상품을 표시한다.
    keyword = request.GET.get("q", "").strip()
    products = [item for item in PRODUCTS if keyword.lower() in item["name"].lower()]
    return render(request, "shop/product_list.html", {"products": products, "keyword": keyword})

def product_detail(request, product_id: int):
    # 존재하지 않는 상품 번호는 HTTP 404로 처리한다.
    product = get_product(product_id)
    if product is None:
        raise Http404("존재하지 않는 상품입니다.")
    return render(request, "shop/product_detail.html", {"product": product})

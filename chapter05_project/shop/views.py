# HTTP 요청을 처리하고 템플릿 또는 JSON을 반환한다.
from django.http import JsonResponse
from django.shortcuts import render

PRODUCTS = [
    {"id": 1, "name": "무선 키보드", "price": 35000, "stock": 5},
    {"id": 2, "name": "무선 마우스", "price": 18000, "stock": 8},
    {"id": 3, "name": "모니터", "price": 190000, "stock": 0},
]

def home(request):
    # 아직 데이터베이스 모델을 만들지 않았으므로 샘플 목록을 전달한다.
    return render(request, "shop/home.html", {"products": PRODUCTS})

def health(request):
    # 서버의 기본 응답 상태를 JSON으로 반환한다.
    return JsonResponse({"status": "ok", "service": "ai-shop"})

# 상품 목록 URL을 뷰 함수에 연결한다.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
]

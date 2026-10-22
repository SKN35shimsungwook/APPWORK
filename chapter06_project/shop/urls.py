# URL 이름을 지정하면 템플릿에서 하드코딩 없이 링크를 생성한다.
from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),
]

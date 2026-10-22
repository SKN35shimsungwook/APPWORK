# 프로젝트 URL에서 shop 앱의 URL로 요청을 전달한다.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
]

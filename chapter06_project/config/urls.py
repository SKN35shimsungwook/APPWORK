# 프로젝트 수준 URL과 앱 URL을 연결한다.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
]

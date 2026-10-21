# 요청 URL을 각 앱의 URL 설정과 연결한다.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
]

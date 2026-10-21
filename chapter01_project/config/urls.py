"""첫 페이지 및 관리자 페이지의 URL을 연결한다."""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# 1장은 템플릿 없이 가장 단순한 HTTP 응답부터 확인한다.
def home(request):
    return HttpResponse("<h1>Chapter 01 Django 실행 성공</h1><p>Python 3.12 + uv</p>")

urlpatterns = [path("admin/", admin.site.urls), path("", home, name="home")]

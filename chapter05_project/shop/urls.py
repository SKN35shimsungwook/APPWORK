# 쇼핑몰의 URL 경로를 정의한다.
from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health, name="health"),
]

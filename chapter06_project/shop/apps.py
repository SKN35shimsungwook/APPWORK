# Django 앱 이름을 등록한다.
from django.apps import AppConfig

class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop"

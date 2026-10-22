# Django가 shop 앱을 인식하도록 등록한다.
from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop"

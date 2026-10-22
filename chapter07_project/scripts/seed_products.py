# Django ORM을 사용하여 기본 상품을 생성하거나 수정한다.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from shop.models import Product

products = [
    ("노트북", 1200000, 5),
    ("마우스", 25000, 30),
    ("키보드", 65000, 12),
]
for name, price, stock in products:
    # 여러 번 실행해도 같은 이름의 상품이 중복 생성되지 않는다.
    Product.objects.update_or_create(name=name, defaults={"price": price, "stock": stock})
print(f"상품 등록 확인: {Product.objects.count()}개")

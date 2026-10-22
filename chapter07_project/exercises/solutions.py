# 과제 1: 가격 기준으로 상품을 조회한다.
# 프로젝트 루트에서 uv run python -m exercises.solutions 명령으로 실행한다.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from shop.models import Product

# 과제 1: 가격이 10만 원 미만인 상품을 출력한다.
cheap_products = Product.objects.filter(price__lt=100000)
print("[과제 1] 10만 원 미만 상품")
for product in cheap_products:
    print(product.name, product.price)
# 과제 2: 재고가 있는 상품 수를 집계한다.
print("[과제 2] 재고 보유 상품 수:", Product.objects.filter(stock__gt=0).count())
# 과제 3: 가장 비싼 상품을 출력한다.
expensive = Product.objects.order_by("-price").first()
print("[과제 3] 최고가 상품:", expensive.name if expensive else "없음")

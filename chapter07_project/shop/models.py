# 제7장은 ORM과 MySQL 연결을 확인하는 기본 상품 모델을 작성한다.
from django.db import models


class Product(models.Model):
    # 상품명을 저장한다.
    name = models.CharField(max_length=100)
    # 가격과 재고는 음수가 될 수 없도록 양의 정수 필드를 사용한다.
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        # 조회 쿼리(Product.objects.all()) 실행 시 별도의 order_by()를 주지 않아도 항상 id 오름차순으로 일관되게 정렬한다.
        ordering = ["id"]

        # id 기준 내림차순(최신 등록순) 정렬
        # ordering = ["-id"]

    def __str__(self):
        return self.name

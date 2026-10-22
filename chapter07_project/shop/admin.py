# Django 관리자 화면에서 상품을 조회할 수 있도록 등록한다.

# Django 프레임워크가 기본 제공하는 관리자 페이지 생성 및 설정 관련 모듈(admin)을 가져옵니다.
from django.contrib import admin

# 현재 앱 패키지(마침표 .) 내의 models.py에 선언된 Product 모델 클래스를 가져옵니다.
from .models import Product


# @admin.register(Product): Product 모델을 관리자 페이지에 등록(Register)하겠다는 선언입니다.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 상품 목록(List view)으로 들어갔을 때, 테이블의 각 행(Row)에 표출할 컬럼(Field)들을 튜플 형태로 지정합니다.
    list_display = ("id", "name", "price", "stock")
    search_fields = ("name",)

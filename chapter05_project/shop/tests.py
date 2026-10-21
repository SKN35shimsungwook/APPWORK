# Django TestCase로 URL·응답·템플릿 렌더링을 검증한다.
from django.test import TestCase
from django.urls import reverse

class ShopViewTests(TestCase):
    def test_home_status(self):
        # 메인 페이지는 HTTP 200을 반환해야 한다.
        response = self.client.get(reverse("shop:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_contains_product(self):
        # 상품명과 HTML이 템플릿에 표시되는지 확인한다.
        response = self.client.get(reverse("shop:home"))
        self.assertContains(response, "무선 키보드")

    def test_health_json(self):
        # 상태 점검 경로가 올바른 JSON을 반환하는지 확인한다.
        response = self.client.get(reverse("shop:health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

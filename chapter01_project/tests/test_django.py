"""Django 첫 화면의 HTTP 응답을 검사한다."""
from django.test import Client

def test_home_page():
    # 테스트 클라이언트로 첫 화면을 요청한다.
    response = Client().get("/")
    assert response.status_code == 200
    assert "Chapter 01 Django 실행 성공" in response.content.decode("utf-8")

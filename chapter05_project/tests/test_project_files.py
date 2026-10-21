"""제5장 프로젝트 파일과 Django 웹 응답을 pytest로 검증한다."""
import ast
from pathlib import Path
from django.urls import reverse

ROOT = Path(__file__).resolve().parents[1]

def test_manage_py_exists():
    # Django 관리 명령 진입점이 생성되었는지 확인한다.
    assert (ROOT / "manage.py").is_file()

def test_project_python_syntax():
    # 프로젝트의 모든 Python 파일을 구문 분석한다.
    for path in ROOT.rglob("*.py"):
        if ".venv" not in path.parts:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

def test_home_status(client):
    # pytest-django가 제공하는 테스트 클라이언트로 메인 화면을 확인한다.
    response = client.get(reverse("shop:home"))
    assert response.status_code == 200

def test_home_product(client):
    # 상품 정보가 HTML 응답에 포함되어 있는지 확인한다.
    response = client.get(reverse("shop:home"))
    assert "무선 키보드" in response.content.decode("utf-8")

def test_health_json(client):
    # 상태 확인 API가 정상 JSON을 반환하는지 검사한다.
    response = client.get(reverse("shop:health"))
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

# 제6장 Django MTV 실습

## 실습 환경
- Windows PowerShell, Python 3.12, uv, VS Code
- Django 5.2.7, python-dotenv, pytest, pytest-django
- 제6장은 SQLite를 사용하며 MySQL은 제7장에서 연결한다.

## 새 폴더에서 순서대로 시작
```powershell
New-Item -ItemType Directory -Force C:\sk-encore\app_workspace\chapter06_project
cd C:\sk-encore\app_workspace\chapter06_project
uv init --python 3.12
uv venv .venv --python 3.12
.\.venv\Scripts\Activate.ps1
# 교재의 pyproject.toml 내용으로 생성된 파일을 수정한다.
uv add "django==5.2.7" "python-dotenv>=1,<2"
uv add --dev "pytest>=8,<10" "pytest-django>=4.8,<5"
# 교재 순서대로 나머지 소스 파일을 작성한다.
Copy-Item .env.example .env
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# 출력된 비밀 키를 .env의 DJANGO_SECRET_KEY에 붙여 넣는다.
uv run python manage.py migrate
uv run python manage.py check
uv run pytest -v
uv run python -m exercises.solutions
uv run python manage.py runserver 127.0.0.1:8000
```

## 접속 주소
- 상품 목록: http://127.0.0.1:8000/
- 상품 상세: http://127.0.0.1:8000/products/1/
- 검색: http://127.0.0.1:8000/?q=마우스

## 파일 생성 규칙
- `uv init`이 만든 `.python-version`과 `pyproject.toml`은 교재 설정으로 수정한다.
- `uv add`가 패키지와 `uv.lock`을 관리한다. 초기 `pyproject.toml`에는 의존성을 중복 선언하지 않는다.
- `config`와 `shop` 패키지는 교재의 파일을 차례대로 작성한다.
- `.env`는 Git에 포함하지 않는다.

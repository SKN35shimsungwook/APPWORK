# 제5장 Git·GitHub와 Django 상품 웹서비스

## 실습 환경
Windows PowerShell, Python 3.12(제1장 설치), uv, VS Code, Git.

## 빈 폴더에서 작성하는 순서
```powershell
New-Item -ItemType Directory -Force C:\sk-encore\app_workspace\chapter05_project
cd C:\sk-encore\app_workspace\chapter05_project
uv init --python 3.12
uv venv .venv --python 3.12
.\.venv\Scripts\Activate.ps1
# ZIP의 pyproject.toml 및 소스 파일을 복사하거나 교재 순서대로 작성
uv add "django==5.2.7" "python-dotenv==1.1.1"
uv add --dev "pytest>=8,<10" "pytest-django>=4.8,<5"
uv sync
uv run python manage.py check
uv run python manage.py migrate
uv run pytest -v
uv run python manage.py runserver 8000
```
`uv init`으로 만든 기본 `pyproject.toml`은 교재 내용으로 수정한다. 소스 ZIP을 압축 해제해 시작했다면 `uv init`, `startproject`, `startapp`을 다시 실행하지 않는다.

## Django 기본 뼈대 생성(직접 작성 실습에만 해당)
```powershell
uv run django-admin startproject config .
uv run python manage.py startapp shop
```
이후 교재에 제시한 파일 내용으로 수정한다.

## Git·GitHub
```powershell
git init
git add .
git commit -m "feat: initialize Django shop"
git branch -M main
# GitHub에서 빈 저장소를 만든 뒤 실제 주소 사용
git remote add origin https://github.com/YOUR-ACCOUNT/chapter05-django-shop.git
git push -u origin main
```
`.env`, `.venv`, `db.sqlite3`는 Git에 포함하지 않는다.

## 접속 주소
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health/

## 참고
제5장은 SQLite로 Django의 기본 흐름을 확인하며, MySQL은 이후 장에서 연동한다.

# 제4장 HTML·CSS·JavaScript 상품 카탈로그

## 제3장과 연결
제3장의 상품 데이터·검색·예외 처리 개념을 브라우저 DOM과 이벤트로 확장한다. 본 장은 독립적인 정적 웹 프로젝트이며 Django 서버는 사용하지 않는다.

## 환경 준비 (Windows PowerShell)
```powershell
mkdir C:\lab\chapter04_project
cd C:\lab\chapter04_project
uv init --python 3.12
uv venv .venv --python 3.12
.\.venv\Scripts\Activate.ps1
```
ZIP 파일을 풀어 생성된 `.python-version`, `pyproject.toml` 등의 파일을 프로젝트 루트에 덮어쓴다. `uv init`이 만든 `main.py`는 본 장에서 사용하지 않으므로 삭제한다.

## 의존성
```powershell
uv add --dev "pytest>=8,<10"
uv sync
uv run pytest -v
```

## 브라우저 실행
```powershell
uv run python -m http.server 8000
```
브라우저에서 http://localhost:8000 을 연다. 종료는 Ctrl+C이다.

## 기대 동작
최초 상품 6개 표시 → 검색 → 장바구니 담기 → 총액 변경 → 삭제/전체 비우기. `pytest`는 HTML/CSS/JS 파일의 정적 구성만 검사하므로 실제 클릭 동작은 브라우저에서 별도로 확인한다.

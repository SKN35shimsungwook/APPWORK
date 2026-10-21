# APPWORK

SKN35 과정 **앱 개발 파트** 실습을 장(章)별로 모아 두는 저장소입니다.
교재를 따라 만든 코드와, 교재를 제 말로 다시 풀어 쓴 풀이노트를 같이 올리고 있습니다.

| 장 | 주제 | 코드 | 풀이노트 | 검증 |
|---|---|---|---|---|
| 1장 | Python 3.12 · uv · VS Code · Django 개발환경 | [chapter01_project](chapter01_project) | [MD](notes/chapter01-풀이노트.md) · [HTML](notes/chapter01-풀이노트.html) | pytest 2 |
| 2장 | Python 기본 문법과 상품 데이터 처리 | [chapter02_project](chapter02_project) | [MD](notes/chapter02-풀이노트.md) | pytest 8 |
| 3장 | Python 모듈·예외 처리·JSON 상품 관리 | [chapter03_project](chapter03_project) | [MD](notes/chapter03-풀이노트.md) | pytest 13 |
| 4장 | HTML·CSS·JavaScript 상품 웹 화면 | [chapter04_project](chapter04_project) | [MD](notes/chapter04-풀이노트.md) | pytest 6 + 브라우저 |
| 5장 | Git·GitHub와 Django 쇼핑몰 프로젝트 | [chapter05_project](chapter05_project) | [MD](notes/chapter05-풀이노트.md) | pytest 5 + Django 3 + 브라우저 |

```mermaid
flowchart LR
    C1[1장<br/>개발환경<br/>uv·Django] --> C2[2장<br/>파이썬 기초<br/>콘솔 쇼핑몰]
    C2 --> C3[3장<br/>모듈 분리<br/>JSON 저장·CLI]
    C3 --> C4[4장<br/>브라우저 화면<br/>HTML·CSS·JS]
    C4 --> C5[5장<br/>Django 템플릿<br/>Git·GitHub]
    C5 -.-> C7[7장 예정<br/>MySQL 연동]
```

같은 "상품 목록·검색·주문"을 장마다 다른 방식으로 다시 만들어 보는 흐름이라, 한 장씩 쌓아 올리는 느낌으로 정리했습니다.

---

## 장별 회고

### 1장 · 개발환경
1장은 코드보다 **환경 세팅**이 대부분이었습니다. `uv init`, `uv venv`, `uv add`, `startproject`처럼 명령을 하나씩 치는데, 각 명령이 무슨 파일을 만들고 그 파일이 무슨 일을 하는지 머릿속에서 연결이 잘 안 됐습니다. 그래서 교재를 "이 명령 → 이 파일 → 이 역할"로 묶어 정리했습니다.
PowerShell 실행 정책을 다섯 번 넘게 바꿨는데, 한 번만 하면 계속 유지된다는 걸 나중에 알았습니다.

### 2장 · 파이썬 기본 문법
변수·조건·반복·함수를 상품 데이터 하나로 연습했습니다. 돈 계산을 실수 대신 정수와 `//`로 하는 이유, 할인율은 `Decimal`로 받는 이유를 처음 제대로 이해했습니다.
가장 인상 깊었던 건 주문 함수에서 **모든 검사를 통과한 뒤에만 재고를 깎는 순서**였습니다. 할인율이 잘못됐는데 재고부터 줄이면 주문은 실패했는데 재고만 사라지는 버그가 생기고, 테스트 하나가 정확히 그걸 잡고 있었습니다.

### 3장 · 모듈과 JSON
2장 코드를 `cli → service → repository` 세 층으로 나눴습니다. 처음엔 파일만 늘어난 것 같았는데, "JSON을 나중에 MySQL로 바꿀 때 repository만 고치면 된다"는 말을 듣고 나서 왜 나누는지 납득이 됐습니다.
`order` 후 다시 `list`를 하면 재고가 그대로 남아 있는 걸 보면서, 2장(끄면 사라짐)과 3장(파일에 남음)의 차이를 몸으로 느꼈습니다.

### 4장 · 브라우저 화면
파이썬 없이 HTML·CSS·JS만으로 상품 카탈로그와 장바구니를 만들었습니다. "데이터(`cart` Map)를 바꾸고 → 화면을 통째로 다시 그린다"는 흐름이 핵심이었습니다.
pytest는 파일 구성만 보기 때문에, 검색·담기·삭제·전체 비우기와 휴대폰 폭 1열 전환은 브라우저에서 직접 눌러 보며 확인했습니다. `innerHTML` 대신 `textContent`를 쓰는 이유(XSS)도 여기서 처음 알았습니다.

### 5장 · Django 쇼핑몰과 Git
4장에서 브라우저가 만들던 화면을 이번엔 **서버가 템플릿으로 만들어 보내도록** 바꿨습니다. 1장은 `urls.py`에 함수를 바로 넣었는데, 5장부터 `shop` 앱을 따로 만들고 `include`로 연결하니 장고 프로젝트다운 구조가 됐습니다.
Git은 이미 쓰고 있었지만 `add → commit → push`가 각각 어디로 옮기는 건지 그림으로 다시 정리했습니다.

---

## 교재대로 했는데 막혔던 것

| 장 | 증상 | 원인 | 해결 |
|---|---|---|---|
| 1 | `KeyError: 'DJANGO_SECRET_KEY'` | PowerShell 5.1의 `Set-Content -Encoding utf8`이 `.env` 앞에 BOM을 붙여 키 이름이 `﻿DJANGO_SECRET_KEY`가 됨 | BOM 없이 저장 (`[IO.File]::WriteAllLines`) |
| 1 | `UnicodeDecodeError: 'cp949'` | hello.py는 UTF-8로 출력하는데 테스트가 한글 Windows 기본값 cp949로 읽음 | `subprocess.run(..., encoding="utf-8")` |
| 2 | `ModuleNotFoundError: No module named 'catalog'` | 교재 `pyproject.toml`에 `pythonpath` 설정이 없음 | `pythonpath = ["."]` 추가 |
| 2 | 테스트가 `shop`을 못 찾음 | 받은 zip의 파일 이름이 `09_shop.py` | 교재대로 `shop.py`로 변경 |
| 3 | `exercises/solutions.py` 실행 시 `catalog` 없음 | 파이썬은 실행한 파일의 폴더(`exercises/`)만 경로에 넣음 | 2장 `answers.py`처럼 `sys.path.insert` 추가 |
| 4 | zip에 pytest 개발 의존성 없음 | 교재의 `uv add --dev` 단계가 zip에 미반영 | `uv add --dev "pytest>=8,<10"` |
| 5 | `verify.ps1` 마지막 줄이 `NO TESTS RAN` | `unittest discover`가 pytest 함수형 테스트를 못 찾음 | `uv run pytest -v`로 변경 |

직접 낸 실수(`cd . 경로`, `--python3.12`, `..venv`, 교재의 `PS>`까지 복사)는 [1장 풀이노트](notes/chapter01-풀이노트.md#제가-실제로-낸-실수들)에 정리했습니다.

## 배운 점
- **uv 하나가 pip + venv + 파이썬 버전 관리를 다 한다.** `pyproject.toml`은 장보기 목록, `uv.lock`은 영수증, `.venv`는 실제로 설치된 곳입니다. uv가 `.venv`를 캐시와 하드링크로 공유한다는 것도 디스크 정리를 하다가 알게 됐습니다.
- **역할을 나누면 바꾸기 쉬워진다.** 2장 단일 파일 → 3장 계층 분리 → 5장 프로젝트/앱 분리로 갈수록, 고칠 곳이 한 군데로 모였습니다.
- **테스트는 무엇을 검사하는지 알아야 한다.** 4장 pytest는 파일 구조만, 5장은 HTTP 응답까지 봅니다. 화면 동작은 결국 직접 눌러 봐야 했습니다.
- **비밀값은 코드에서 분리한다.** `.env`로 빼고, `.gitignore`로 막고, `.env.example`만 공유합니다.
- **에러 메시지의 겉모습만 믿으면 안 된다.** 교재를 그대로 따라 했는데 나는 오류가 7개였고, 대부분 한글 Windows 환경이나 경로 문제였습니다.

---

## 실행 방법

Windows PowerShell 기준입니다. [uv](https://docs.astral.sh/uv/)가 설치되어 있어야 합니다.

```powershell
git clone https://github.com/SKN35shimsungwook/APPWORK.git
cd APPWORK
uv python install 3.12
```

### 1장
```powershell
cd chapter01_project
uv sync
Copy-Item .env.example .env
$secret = uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
$lines = (Get-Content .env) -replace '^DJANGO_SECRET_KEY=.*$', "DJANGO_SECRET_KEY=$secret"
[IO.File]::WriteAllLines("$PWD\.env", $lines)
uv run python manage.py migrate
uv run pytest -v
uv run python manage.py runserver 127.0.0.1:8000    # "Chapter 01 Django 실행 성공"
```

### 2장
```powershell
cd chapter02_project
uv sync
uv run python shop.py              # 주문: 무선 키보드 2개 / 63,000원
uv run pytest -v                   # 8 passed
uv run python exercises/answers.py
```

### 3장
```powershell
cd chapter03_project
uv sync
uv run python main.py list
uv run python main.py search 키보드
uv run python main.py order 1 2    # 재고가 data/products.json에 저장됨
uv run pytest -v                   # 13 passed
uv run python exercises/solutions.py
```
처음 상태로 돌리려면 `data/products.json`을 지웁니다.

### 4장
```powershell
cd chapter04_project
uv sync
uv run pytest -v                       # 6 passed
uv run python -m http.server 8000      # http://localhost:8000
```

### 5장
```powershell
cd chapter05_project
uv sync
uv run python manage.py migrate
uv run pytest -v                       # 5 passed
uv run python manage.py test shop      # 3 tests OK
uv run python manage.py runserver 8000 # http://127.0.0.1:8000/ , /health/
```
`.\scripts\verify.ps1` 한 줄로 위 검사를 한 번에 돌릴 수도 있습니다. 5장은 `.env`가 없어도 개발용 기본 키로 실행됩니다.

## 검증 결과 (제 PC에서 직접 실행)

| 장 | 검사 | 결과 |
|---|---|---|
| 1 | `pytest` / `check` / `runserver` | 2 passed / no issues / `GET /` 200 |
| 2 | 01~08 예제, `shop.py`, `answers.py` | 교재 출력과 모두 일치, 8 passed |
| 3 | `list → order 1 2 → list`, `order 999 1` | 재고 5→3 저장, 오류 시 종료 코드 1, 13 passed |
| 4 | 브라우저 조작 | 6개 표시 → 검색 1개 → 담기 총액 207,000원 → 삭제 → 비우기 0원, 375px에서 1열 |
| 5 | `check` / `pytest` / `test shop` / 브라우저 | no issues / 5 passed / 3 OK / 카드 3개·품절 표시·`/health/` ok |

---

## 기술 스택

| 항목 | 버전 |
|---|---|
| OS | Windows 11 · PowerShell 5.1 |
| Python | 3.12.x (uv 관리) |
| 패키지 관리 | uv |
| 웹 | HTML · CSS · JavaScript (4장), Django 5.2.7 (1·5장) |
| 환경변수 | python-dotenv 1.1.1 |
| 테스트 | pytest 8~9, pytest-django 4.8~ |
| 데이터 | 메모리(2장) → JSON 파일(3장) → SQLite(1·5장) → MySQL(7장 예정) |

## 폴더 구조

```
APPWORK/
├── README.md
├── notes/                         # 장별 풀이노트 (mermaid 그림 포함)
│   ├── chapter01-풀이노트.md · .html
│   ├── chapter02-풀이노트.md
│   ├── chapter03-풀이노트.md
│   ├── chapter04-풀이노트.md
│   └── chapter05-풀이노트.md
├── chapter01_project/             # Django 개발환경 (config/, hello.py, tests/)
├── chapter02_project/             # 01~08 문법 예제, catalog.py, shop.py, tests/
├── chapter03_project/             # main.py, catalog/(cli·service·repository·exceptions), tests/
├── chapter04_project/             # index.html, assets/(style.css·app.js), tests/
└── chapter05_project/             # config/, shop/(views·urls·templates·static), tests/, scripts/verify.ps1
```

## 참고
- 교재 PDF는 올리지 않았고, 풀이노트는 제가 다시 쓴 요약입니다.
- `.env`, `.venv/`, `db.sqlite3`, 실행 중 생기는 `products.json`은 `.gitignore`로 제외되어 있어서 저장소에 비밀키가 없습니다.

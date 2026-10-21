# APPWORK

SKN35 과정 **앱 개발 파트** 실습을 장(章)별로 모아 두는 저장소입니다.
교재를 따라 만든 코드와, 교재를 제 말로 다시 풀어 쓴 풀이노트를 같이 올리고 있습니다.

| 장 | 주제 | 코드 | 풀이노트 |
|---|---|---|---|
| 1장 | Python 3.12 · uv · VS Code · Django 5.2.7 개발환경 | [chapter01_project](chapter01_project) | [Markdown](notes/chapter01-풀이노트.md) · [HTML](notes/chapter01-풀이노트.html) |

---

## 1장을 하면서

### 왜 정리했나
1장은 코드보다 **환경 세팅**이 대부분이었습니다. `uv init`, `uv venv`, `uv add`, `startproject`처럼 명령을 하나씩 치는데, 각 명령이 무슨 파일을 만들고 그 파일이 무슨 일을 하는지 머릿속에서 연결이 잘 안 됐습니다.
그래서 교재 33쪽을 처음부터 끝까지 다시 읽으면서 "이 명령 → 이 파일 → 이 역할"로 묶어 정리했고, 직접 낸 실수도 같이 적어 두었습니다.

### 진행 과정
1. PowerShell 실행 정책을 `RemoteSigned`로 바꿨습니다. 같은 명령을 다섯 번 넘게 쳤는데, 한 번만 하면 계속 유지된다는 걸 나중에 알았습니다.
2. `uv init chapter01_project --python 3.12`로 프로젝트를 만들고, `uv venv`로 가상환경을 만들었습니다.
3. `uv add "django==5.2.7" "python-dotenv==1.1.1"`로 장고를 설치하고, `uv add --dev`로 pytest를 넣었습니다.
4. `uv run django-admin startproject config .`로 뼈대를 만들고, 교재 코드로 `settings.py`, `urls.py` 등을 바꿨습니다.
5. `.env`에 비밀키를 넣고 `check → migrate → pytest → runserver` 순서로 검증했습니다.

### 막혔던 것과 해결
| 증상 | 원인 | 해결 |
|---|---|---|
| `cd . C:\...` 오류 | 경로 앞에 점이 하나 더 붙음 | `cd C:\...` |
| `--python3.12` 인식 안 됨 | 옵션과 값 사이 띄어쓰기 누락 | `--python 3.12` |
| `..venv` 모듈 로드 실패 | `..`은 상위 폴더라는 뜻 | `.venv\Scripts\activate` |
| `PS>` 용어 인식 안 됨 | 교재의 프롬프트 표시까지 복사 | `PS>` 빼고 입력 |
| `KeyError: 'DJANGO_SECRET_KEY'` | PowerShell 5.1의 `Set-Content -Encoding utf8`이 `.env` 앞에 BOM을 붙여 키 이름이 `\ufeffDJANGO_SECRET_KEY`가 됨 | BOM 없이 저장 (`[IO.File]::WriteAllLines`) |
| `test_hello` 실패 (`UnicodeDecodeError: 'cp949'`) | hello.py는 UTF-8로 한글을 출력하는데 테스트가 한글 Windows 기본값 cp949로 읽음 | `subprocess.run(..., encoding="utf-8")` + `PYTHONIOENCODING=utf-8` |

마지막 두 개는 교재를 그대로 따라 해도 한글 Windows에서는 나는 오류라서 따로 원인을 찾아야 했습니다. 오류 메시지만 보면 비밀키가 없는 것처럼 보이는데, 실제로는 파일 맨 앞의 보이지 않는 3바이트 때문이었습니다.

### 배운 점
- **uv 하나가 pip + venv + 파이썬 버전 관리를 다 한다.** `pyproject.toml`은 장보기 목록, `uv.lock`은 영수증, `.venv`는 실제로 설치된 곳이라고 생각하니 `uv add`와 `uv sync`의 차이가 이해됐습니다.
- **장고는 웹사이트에 늘 필요한 기능을 미리 만들어 둔 도구 상자다.** 이번에 직접 쓴 코드는 `home()` 함수 세 줄이고, 보안 검사·세션·관리자 페이지는 `INSTALLED_APPS`와 `MIDDLEWARE`에 이미 들어 있었습니다.
- **비밀값은 코드에서 분리한다.** `SECRET_KEY`를 `.env`로 빼고, `.gitignore`로 막고, `.env.example`만 공유하는 흐름을 처음 제대로 해 봤습니다.
- **에러 메시지의 겉모습만 믿으면 안 된다.** KeyError가 났지만 키는 분명히 있었고, 바이트를 직접 열어 보고서야 원인을 찾았습니다.

---

## 1장 실행 방법

Windows PowerShell 기준입니다. [uv](https://docs.astral.sh/uv/)가 설치되어 있어야 합니다.

```powershell
git clone https://github.com/SKN35shimsungwook/APPWORK.git
cd APPWORK\chapter01_project

uv python install 3.12
uv sync                                  # pyproject.toml + uv.lock 대로 패키지 설치
Copy-Item .env.example .env

# 비밀키를 만들어 .env에 BOM 없이 저장
$secret = uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
$lines = (Get-Content .env) -replace '^DJANGO_SECRET_KEY=.*$', "DJANGO_SECRET_KEY=$secret"
[IO.File]::WriteAllLines("$PWD\.env", $lines)

uv run python check_environment.py       # Python 3.12 / Django 5.2.7
uv run python manage.py check            # System check identified no issues
uv run python manage.py migrate          # db.sqlite3 기본 테이블 생성
uv run pytest -v                         # 2 passed
uv run python manage.py runserver 127.0.0.1:8000
```

브라우저에서 http://127.0.0.1:8000/ 에 들어가면 **"Chapter 01 Django 실행 성공"** 이 보입니다. 서버는 `Ctrl + C`로 끕니다.

### 검증 결과
| 검사 | 결과 |
|---|---|
| `hello.py` | `프로젝트: chapter01-development` / `Python 버전: 3.12` |
| `check_environment.py` | `Python: 3.12` / `Django: 5.2.7` |
| `manage.py check` | System check identified no issues (0 silenced). |
| `manage.py migrate` | admin, auth, contenttypes, sessions 마이그레이션 OK |
| `pytest -v` | `test_django.py::test_home_page PASSED`, `test_hello.py::test_hello_output PASSED` |
| `runserver` | `GET /` → 200, "Chapter 01 Django 실행 성공" |

---

## 기술 스택

| 항목 | 버전 |
|---|---|
| OS | Windows 11 · PowerShell 5.1 |
| Python | 3.12.x (uv 관리) |
| 패키지 관리 | uv |
| 웹 프레임워크 | Django 5.2.7 |
| 환경변수 | python-dotenv 1.1.1 |
| 테스트 | pytest 8~9, pytest-django 4.8~ |
| DB | SQLite (7장에서 MySQL로 전환 예정) |

## 폴더 구조

```
APPWORK/
├── README.md
├── notes/
│   ├── chapter01-풀이노트.md      # GitHub에서 바로 읽는 버전 (mermaid 그림 포함)
│   └── chapter01-풀이노트.html    # 내려받아 브라우저로 여는 버전 (파일 탐색기·점검표)
└── chapter01_project/
    ├── .env.example               # 환경변수 견본 (.env는 Git 제외)
    ├── .gitignore
    ├── .python-version            # 3.12
    ├── pyproject.toml             # 프로젝트·의존성·pytest 설정
    ├── uv.lock                    # 의존성 잠금
    ├── manage.py                  # 장고 관리 명령 입구
    ├── config/
    │   ├── settings.py            # .env 로드, SECRET_KEY·DEBUG, 앱·미들웨어, SQLite
    │   ├── urls.py                # admin/ 과 첫 화면 home()
    │   ├── asgi.py · wsgi.py      # 배포용 서버 진입점
    │   └── __init__.py
    ├── hello.py                   # 파이썬 동작 확인
    ├── check_environment.py       # 환경 진단
    └── tests/
        ├── test_hello.py
        └── test_django.py
```

## 참고
- 교재: 「제1장. Python 3.12 · uv · VS Code · Django」. 교재 PDF는 올리지 않았고, 풀이노트는 제가 다시 쓴 요약입니다.
- `.env`, `.venv/`, `db.sqlite3`는 `.gitignore`로 제외되어 있어서 저장소에 비밀키가 없습니다.

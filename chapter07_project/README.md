# 제7장 Docker · MySQL 설치 및 SQL 기초

## 환경
- Windows PowerShell, Python 3.12, uv, Docker Desktop (Linux 컨테이너 모드)
- MySQL 8.4 컨테이너, Django 5.2.7, mysqlclient, pytest, pytest-django

## 새 프로젝트를 직접 작성하는 경우
```powershell
New-Item -ItemType Directory -Force C:\sk-encore\app_workspace\chapter07_project
Set-Location C:\sk-encore\app_workspace\chapter07_project
uv init --python 3.12
uv venv .venv --python 3.12
.\.venv\Scripts\Activate.ps1
# 교재의 pyproject.toml과 나머지 파일을 작성한다.
uv add "django==5.2.7" "mysqlclient>=2.2.7,<3" "python-dotenv>=1,<2"
uv add --dev "pytest>=8,<10" "pytest-django>=4.8,<5"
```

## ZIP을 압축 해제하여 실행하는 경우
```powershell
cd C:\sk-encore\app_workspace\chapter07_project
uv sync
Copy-Item .env.example .env
# .env의 MySQL 비밀번호를 반드시 변경한다.
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# 출력된 값을 .env의 DJANGO_SECRET_KEY에 입력한다.
docker compose up -d
# docker compose ps 명령으로 mysql 서비스가 healthy인지 확인한다.
docker compose ps
uv run python manage.py migrate
uv run python -m scripts.seed_products
uv run python manage.py runserver 127.0.0.1:8000
```
브라우저 주소: http://127.0.0.1:8000/

## SQL 실습
```powershell
# 호스트의 MySQL 클라이언트 설치 없이 컨테이너 안에서 실행한다.
# --default-character-set=utf8mb4가 없으면 컨테이너 기본값(latin1) 때문에 한글이 깨진다.
docker compose exec mysql sh -c 'MYSQL_PWD="$MYSQL_PASSWORD" mysql -u"$MYSQL_USER" "$MYSQL_DATABASE" --default-character-set=utf8mb4'
# 위 명령으로 열린 mysql> 프롬프트에서 SQL 문장을 실행한다.
# sql/practice/03_queries.sql 파일의 문장을 순서대로 붙여넣는다.
```

## 테스트
```powershell
# MySQL 컨테이너 실행 상태에서 테스트한다.
# 테스트 DB(test_shopdb) 권한은 sql/03_test_privileges.sh가 첫 실행 때 자동으로 준다.
uv run pytest -v
uv run python -m exercises.solutions
```

## 종료
```powershell
docker compose down
# 데이터까지 삭제하는 아래 명령은 실습을 완전히 초기화할 때만 사용한다.
# docker compose down -v
```

참고: sql/ 바로 아래의 01_schema.sql, 02_seed.sql, 03_test_privileges.sh는 MySQL 볼륨이 비어 있는 최초 시작에만 자동 실행된다. 연습용 SQL은 자동 실행되지 않도록 sql/practice/에 둔다.
참고: `.env`는 Git에 올리지 않는다. 배포 시에는 DEBUG=False 및 적절한 ALLOWED_HOSTS와 비밀 관리가 필요하다.

## 교재와 다르게 한 곳
- `config/settings.py`에 `STATICFILES_DIRS = [BASE_DIR / "static"]`를 추가했다. 교재 설정만으로는 프로젝트 루트의 `static/shop/style.css`를 찾지 못해 CSS가 404가 된다.
- SQL 파일 맨 위에 `SET NAMES utf8mb4;`를 넣었다. 컨테이너의 mysql 클라이언트 기본 문자셋이 latin1이라 초기화 때 '노트북'이 'ë…¸íŠ¸ë¶'처럼 깨져 저장됐다.
- `03_queries.sql`을 `sql/practice/`로 옮겼다. `sql/` 바로 아래의 .sql은 첫 실행 때 모두 자동 실행되어, 연습용 UPDATE(마우스 재고 -1)가 미리 적용돼 버렸다.
- `sql/03_test_privileges.sh`를 추가했다. MySQL 이미지는 MYSQL_USER에게 shopdb 권한만 줘서 pytest가 test_shopdb를 만들지 못하고 `Access denied`(1044)로 실패했다.
- `.gitattributes`로 `*.sh`를 LF 줄바꿈으로 고정했다. Windows 줄바꿈(CRLF)이면 컨테이너 안의 bash가 스크립트를 실행하지 못한다.

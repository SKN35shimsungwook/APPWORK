# 제1장 개발환경 실습 프로젝트

Windows PowerShell에서 다음 순서대로 실행한다.

```powershell
uv python install 3.12
uv sync
Copy-Item .env.example .env
$secret = uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
$lines = (Get-Content .env) -replace '^DJANGO_SECRET_KEY=.*$', "DJANGO_SECRET_KEY=$secret"
[IO.File]::WriteAllLines("$PWD\.env", $lines)
uv run python hello.py
uv run python check_environment.py
uv run python manage.py check
uv run python manage.py migrate
uv run pytest -q
uv run python manage.py runserver 127.0.0.1:8000
```

브라우저: http://127.0.0.1:8000/

`.env`는 비공개이며 `.env.example`만 공유한다. MySQL은 제7장에서 연결한다.

> 교재의 `Set-Content .env -Encoding utf8`은 Windows PowerShell 5.1에서 파일 앞에 BOM을 붙인다.
> 그러면 python-dotenv가 키 이름을 `﻿DJANGO_SECRET_KEY`로 읽어 KeyError가 나므로, BOM 없이 저장하는 `[IO.File]::WriteAllLines`를 쓴다.

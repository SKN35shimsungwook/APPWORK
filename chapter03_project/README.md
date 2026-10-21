# 제3장: 모듈·예외·JSON 상품 관리

Windows PowerShell에서 프로젝트 폴더로 이동한다.

```powershell
uv python install 3.12
uv sync
uv run python main.py list
uv run python main.py search 키보드
uv run python main.py order 1 2
uv run python main.py list
uv run pytest -v
uv run python exercises/solutions.py
```

`order` 실행 시 `data/products.json`이 생성되며 재고가 저장된다. 반복 실습을 초기화하려면 해당 파일을 삭제한다. `tests/conftest.py`는 pytest가 자동으로 로드하므로 직접 실행하지 않는다. Django와 MySQL은 이 장에서 사용하지 않는다.

## Windows PowerShell: 가상환경 생성 및 활성화

```powershell
# 최초 1회 uv 설치
irm https://astral.sh/uv/install.ps1 | iex
# Python 3.12 설치 및 가상환경 생성
uv python install 3.12
uv venv --python 3.12
# 가상환경 활성화 (선택 사항)
.\.venv\Scripts\Activate.ps1
# pyproject.toml 의존성 설치
uv sync
# 프로그램 실행 및 pytest
uv run python main.py list
uv run pytest -v
# 활성화했다면 종료
deactivate
```

활성화하지 않아도 `uv run`은 프로젝트 가상환경을 사용한다. PowerShell 활성화가 정책에 의해 차단되면 현재 세션에 한해 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`를 실행할 수 있다.

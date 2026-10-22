# 프로젝트 최상위 폴더에서 실행한다.
$ErrorActionPreference = "Stop"
uv run python manage.py check
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
uv run pytest -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "제6장 검증 완료"

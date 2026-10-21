# Python 버전과 의존성을 동기화한다.
uv python install 3.12
uv sync
# 프로젝트 설정을 점검한다.
uv run python manage.py check
# 데이터베이스 마이그레이션을 적용한다.
uv run python manage.py migrate
# Django 테스트를 실행한다.
uv run python manage.py test shop -v 2
# 파일 구조와 웹 응답을 pytest로 검증한다.
# (교재의 unittest discover는 pytest 함수형 테스트를 찾지 못해 0개 실행으로 끝나므로 pytest로 바꿨다.)
uv run pytest -v

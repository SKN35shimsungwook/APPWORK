"""제3장 프로그램의 실행 진입점."""
from catalog.cli import main

# 이 파일을 직접 실행할 때만 CLI를 시작한다.
if __name__ == "__main__":
    raise SystemExit(main())

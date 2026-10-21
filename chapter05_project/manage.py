# Django 관리 명령의 시작점이다.
import os
import sys

def main():
    # Django가 사용할 설정 모듈을 지정한다.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    # 명령줄 인자를 Django 관리 명령에 전달한다.
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

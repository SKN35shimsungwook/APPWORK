# Django 관리 명령 실행 파일이다.
import os
import sys


def main():
    # Django 설정 모듈을 지정한다.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

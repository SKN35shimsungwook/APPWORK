# Django 관리 명령을 실행하는 진입점이다.
import os
import sys

def main():
    # 프로젝트 설정 모듈의 위치를 지정한다.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

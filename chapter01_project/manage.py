#!/usr/bin/env python
"""Django 관리 명령의 진입점이다."""
import os
import sys

if __name__ == "__main__":
    # Django가 사용할 설정 모듈을 지정한다.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

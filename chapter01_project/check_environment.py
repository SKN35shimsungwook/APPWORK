"""Django 설치 및 실행환경을 확인한다."""
import sys
import django

# Python 3.12를 사용하고 있는지 검사한다.
assert sys.version_info[:2] == (3, 12), "Python 3.12 환경에서 실행해야 한다."
print(f"Python: {sys.version_info.major}.{sys.version_info.minor}")
print(f"Django: {django.get_version()}")

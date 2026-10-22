# 일반적인 WSGI 서버에서 Django 앱을 호출하는 진입점이다.
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

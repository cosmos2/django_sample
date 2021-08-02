from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    ".localhost",
]

# 모든 도메인 허용
CSRF_COOKIE_DOMAIN = None
CSRF_TRUSTED_ORIGINS = []

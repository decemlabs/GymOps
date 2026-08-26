"""Production settings: every value comes from the environment."""

from .base import *  # noqa: F403

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# Collected by `manage.py collectstatic` at build time, never committed.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# HTTPS is terminated by the reverse proxy; trust its header and refuse
# to serve anything over plain HTTP.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

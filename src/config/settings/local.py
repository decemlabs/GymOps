"""Development settings: this machine, DEBUG on, no secrets required."""

from .base import *  # noqa: F403
from .base import env

# Development only. Production reads the key from the environment and
# refuses to start without it.
SECRET_KEY = env.str(
    'DJANGO_SECRET_KEY',
    default='django-insecure-local-only-v4t4ct=%jin)k-c^#9%6eu8j%+d87lg)v)3k',
)

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

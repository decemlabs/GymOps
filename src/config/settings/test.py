"""Test settings: fast and deterministic, no secrets required."""

from .base import *  # noqa: F403

SECRET_KEY = 'django-insecure-test-only'

DEBUG = False

# The default hasher is deliberately slow; tests create users by the dozen.
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

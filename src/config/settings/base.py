"""
Base settings shared by every environment.

Files describe the structure and the differences between environments,
environment variables supply the values and the secrets (ADR-0005).
This module is never used directly: pick config.settings.local,
config.settings.production or config.settings.test.
"""

from pathlib import Path

import environ

# src/config/settings/base.py -> repository root
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SRC_DIR = BASE_DIR / 'src'

env = environ.Env()

# The process environment wins; .env only fills in what it does not define.
# Locally that means no shell export; in production there is no .env file and
# every value comes from the container environment.
environ.Env.read_env(BASE_DIR / '.env')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [SRC_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', default='gymops'),
        'USER': env.str('POSTGRES_USER', default='postgres'),
        # No default: the process must fail on start, not on the first query.
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST', default='localhost'),
        'PORT': env.int('POSTGRES_PORT', default=5432),
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Stored time is UTC everywhere; a club's own timezone is its own attribute.
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static and media files
# https://docs.djangoproject.com/en/6.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [SRC_DIR / 'static']

# Uploads live outside src/: they are runtime data, not source code.
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

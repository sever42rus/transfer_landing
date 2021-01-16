import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR / 'db.sqlite3',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]
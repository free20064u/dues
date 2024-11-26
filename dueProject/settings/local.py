from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = 'static'
MEDIA_ROOT = BASE_DIR/'media' # Directory where uploaded 

LIVERELOAD_HOST = '192.168.43.180'
LIVERELOAD_PORT = '35729'
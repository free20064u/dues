from .base import *
DEBUG = True

ALLOWED_HOSTS = ['wbmzionscience.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': os.getenv('NAME'),
# 		'USER': os.getenv('USER'),
# 		'PASSWORD':os.getenv('PASSWORD'),
# 		'HOST':os.getenv('HOST'),
# 		'PORT':os.getenv('PORT'),
# 	}
# }


MEDIA_ROOT = BASE_DIR/'media'
STATIC_ROOT = BASE_DIR / "staticfiles"
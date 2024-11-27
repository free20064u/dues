from .base import *
DEBUG = False

DEBUG = os.getenv('DEBUG')
SECRET_KEY= os.getenv('SECRET_KEY')
ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fontawesomefree',
    'accounts',
    'base',
    'main',
    'extraction',
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

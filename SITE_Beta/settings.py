from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-wk!u_8k)8f(e)i=k(#@d86cdk5lfwo58&fgjd1uqy87&nag$4r'

DEBUG = True

ALLOWED_HOSTS = ['*']  # Permitimos todas las solicitudes por ahora

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'Siteone'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'SITE_Beta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SITE_Beta.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbsite',
        'USER': 'root',
        'PASSWORD': 'NvrCnOqoXLUsiPHyvbwfRirXIBjVVijP',
        'HOST': 'centerbeam.proxy.rlwy.net',
        'PORT': '32108',
        'CONN_MAX_AGE': 45,
        'CONN_HEALTH_CHECKS': True,
    }
}

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

LANGUAGES = [
    ('es', ('Spanish')),
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# AGREGA ESTA LÍNEA (para que Django reconozca la carpeta static de tu proyecto):
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, '')
MEDIA_URL = '/images/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ID_ESTADO = '0'
ID_PARTIDO = '1'
ID_USUARIO='0'

# Aumentar el tamaño máximo permitido para la carga de datos a 25MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 200 * 1024 * 1024  # Tamaño en bytes (200MB)




CSRF_TRUSTED_ORIGINS = [
    'https://site-production-d80a.up.railway.app',
]
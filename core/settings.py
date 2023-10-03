import environ
import os
import dj_database_url

from pathlib import Path
from configurations import Configuration, values

env = environ.Env()


class Dev(Configuration):
    
    # Set base directory
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Read variables from .env
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(['*', 'localhost'])

    # App's definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
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
        ]

    ROOT_URLCONF = 'core.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'core.wsgi.application'

    # Database
    DATABASES = values.DatabaseURLValue('sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))

    # Password validation
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
    LANGUAGE_CODE = 'pt-BR'
    TIME_ZONE = values.Value('America/Sao_Paulo')
    USE_I18N = values.BooleanValue(True)
    USE_TZ = values.BooleanValue(True)

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    # Default primary key field type
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



class Prod(Dev):    
    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(True)

    USE_THOUSAND_SEPARATOR = values.BooleanValue(True)

    USE_L10N = True

    DATABASES = {
        'default': dj_database_url.config(default=os.environ["DATABASE_URL"]),
    }

    # FORM SUBMISSION
    #CSRF_ALLOWED_ORIGINS = ['https://up.railway.app'] 
    #CSRF_TRUSTED_ORIGINS = ['https://up.railway.app']
    #CORS_ORIGINS_WHITELIST = ['https://up.railway.app']


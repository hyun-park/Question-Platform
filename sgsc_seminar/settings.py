"""
Django settings for sgsc_seminar project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json

import django_heroku

import dj_database_url

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#awzw+8#8cd_wzd1^o6=(+$9-_4^60cnv9l*l(bqu0#&wu@mp9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'questions',
    'social_django',
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

ROOT_URLCONF = 'sgsc_seminar.urls'

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

WSGI_APPLICATION = 'sgsc_seminar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2', # Google
    'social_core.backends.facebook.FacebookOAuth2', # Facebook
    'django.contrib.auth.backends.ModelBackend', # Django 기본 유저모델
]

# Env for dev / deploy
def get_env(setting, envs):
    try:
        return envs[setting]
    except KeyError:
        error_msg = "You SHOULD set {} environ".format(setting)
        raise ImproperlyConfigured(error_msg)

DEV_ENVS = os.path.join(BASE_DIR, "envs_dev.json")
DEPLOY_ENVS = os.path.join(BASE_DIR, "envs.json")

if os.path.exists(DEV_ENVS): # Develop Env
    env_file = open(DEV_ENVS)
elif os.path.exists(DEPLOY_ENVS): # Deploy Env
    env_file = open(DEPLOY_ENVS)
else:
    env_file = None

if env_file is None: # System environ
    try:
        GOOGLE_KEY = os.environ['GOOGLE_KEY']
        GOOGLE_SECRET = os.environ['GOOGLE_SECRET']
        FACEBOOK_KEY = os.environ['FACEBOOK_KEY']
        FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']
    except KeyError as error_msg:
        raise ImproperlyConfigured(error_msg)
else: # JSON env
    envs = json.loads(env_file.read())
    FACEBOOK_KEY = get_env('FACEBOOK_KEY', envs)
    FACEBOOK_SECRET = get_env('FACEBOOK_SECRET', envs)
    GOOGLE_KEY = get_env('GOOGLE_KEY', envs)
    GOOGLE_SECRET = get_env('GOOGLE_SECRET', envs)

SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}


# SocialLogin: Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = GOOGLE_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = GOOGLE_SECRET
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

django_heroku.settings(locals())
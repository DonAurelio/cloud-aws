 # -*- coding: utf-8 -*-

"""
Django settings for aucarvideo project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cheking if the application is running in a production environment
PRODUCTION = True if os.environ.get('PRODUCTIO','') else False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if PRODUCTION else True

ALLOWED_HOSTS = ['*']

# Mail settings

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND','')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','')

EMAIL_HOST = os.environ.get('EMAIL_HOST','')
EMAIL_PORT = os.environ.get('EMAIL_PORT','')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD','')
EMAIL_USE_TLS = True


INSTALLED_APPS = (
    'home',
    'profile',
    'contests',

    # django apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    # To serve django admin staticfiles
    'django.contrib.staticfiles',

    # Others  Apps
    'bootstrap3',
)


MIDDLEWARE = [
    # For django-tenant-schemas
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
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

WSGI_APPLICATION = 'aucarvideo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ.get('DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
    'HOST': os.environ.get('DB_HOST') ,
    'PORT': os.environ.get('DB_PORT')
    }
}

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

if not PRODUCTION:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

if PRODUCTION:
    STATIC_ROOT = os.path.join(BASE_DIR,"static")

# The storage API will not isolate media per tenant. 
# Your MEDIA_ROOT will be a shared space between all tenants.

# To avoid this you should configure a tenant aware storage
# backend - you will be warned if this is not the case.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Celery settings
BROKER_URL =os.environ.get('BROKER_URL')

# IF we use AWS SQS
if 'sqs' in BROKER_URL:
    # BROKER_URL = "sqs://"
    BROKER_TRANSPORT_OPTIONS = {
        'region': 'us-west-2',
        'polling_interval': 20,
        "queue_name_prefix": "aucar-sqs-C-"
    }

    CELERY_RESULT_BACKEND = None


ROOT_URLCONF = 'aucarvideo.urls'

# S3 settings
S3_BUCKET_NAME = 'aucarvideobucket'
# FRONT_CONTENT_URL_FORMAT = 'https://s3-us-west-2.amazonaws.com/aucarvideobucket/{s3_obj_key}'
FRONT_CONTENT_URL_FORMAT = 'http://d145tcqebewora.cloudfront.net/{s3_obj_key}'
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
PRODUCTION = True if 'PRODUCTION' in os.environ else False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if PRODUCTION else True

ALLOWED_HOSTS = ['*']

# The name of the tenant model
TENANT_MODEL = "customers.Client"

# The domain name for the public tenant.
# This constant is used also as base for all 
# tenants urls created on the aplication. 
# For example: a new tenant example1
# will have example1.aucarvideo.com url.
DOMAIN_NAME = 'aucarvideo.com'

# When a tenant is created, we need to redirec to
# specific tenant url. If we are in development this 
# tenant will run over the 8000 for, but, in production
# will run over the 80
# we use this contant on 'customer.views'. 
CREATED_TENANT_REDIRECTION_PORT = '80' if PRODUCTION else '8000' 

# Mail settings
if 'AWS_EMAIL' in os.environ:
    EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND','')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','')

EMAIL_HOST = os.environ.get('EMAIL_HOST','')
EMAIL_PORT = os.environ.get('EMAIL_PORT','')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD','')
EMAIL_USE_TLS = True

# Application definition

# These apps models will be created in the public schema 
SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app

    # everything below here is optional
    'customers',
    'home_public',

    # django apps
    # 'django.contrib.contenttypes',
    # 'django.contrib.auth',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.admin',
)

# This apps models will be replicated in schemas
TENANT_APPS = (
    # your tenant-specific apps
    
    # 'login',
    'auth_tenants',
    'home_tenants',
    'contests',

    # django apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
)

INSTALLED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app

    # your tenant-specific apps
    'customers',
    'home_public',
    'auth_tenants',
    'home_tenants',
    'contests',
    # 'login',
    # 'home_tenats',

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

# For django-tenant-schemas
# Add the middleware tenant_schemas.middleware.TenantMiddleware 
# to the top of MIDDLEWARE_CLASSES, so that each request can be 
# set to use the correct schema.

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

if not PRODUCTION:
    # For django-tenant-schemas
    MIDDLEWARE = ['tenant_schemas.middleware.TenantMiddleware'] + MIDDLEWARE

if PRODUCTION:
    # For django-tenant-schemas
    MIDDLEWARE = ['customers.middleware.XHeaderTenantMiddleware'] + MIDDLEWARE


# URLs for the tenants
ROOT_URLCONF = 'aucarvideo.urls_tenants'
# URL for the public application
PUBLIC_SCHEMA_URLCONF = 'aucarvideo.urls_public'

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
    'ENGINE': 'tenant_schemas.postgresql_backend',
    #'NAME': os.environ.get('DB_NAME' if PRODUCTION else 'POSTGRES_DB'),
    'NAME': os.environ.get('DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
    # If your are in development put in '' the IP addres
    # of the postgres server
    'HOST': os.environ.get('DB_HOST') ,
    'PORT': os.environ.get('DB_PORT')
    }
}

# Add tenant_schemas.routers.TenantSyncRouter to your DATABASE_ROUTERS setting, 
# so that the correct apps can be synced, depending on what’s being synced (shared or tenant).
DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

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

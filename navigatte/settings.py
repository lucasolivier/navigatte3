"""
Django settings for navigatte project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['NVGTT_SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
#If we are in production env
if "BLUEMIX_REGION" in os.environ:
    DEBUG = False
else: #non production env
    DEBUG = True

#Set allowed hosts for prod/dev enviraonemnt
#If we are in production env
if "BLUEMIX_REGION" in os.environ:
    ALLOWED_HOSTS = ["nvgtt.mybluemix.net", "navigatte.com"]
else: #non production env
    ALLOWED_HOSTS = ["*"]


#Security stuff

#If we are in production env
if "BLUEMIX_REGION" in os.environ:

    SECUREFLAG = False
    
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = SECUREFLAG
    SESSION_COOKIE_SECURE = SECUREFLAG
    CSRF_COOKIE_SECURE = SECUREFLAG

    if not SECUREFLAG:
        print("WARNING! SECURE FLAG IS TURNED OFF.")

#Register disable flag
REGISTER_DISABLED = False

#Login required url
LOGIN_URL = "/login/"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'topics',
    'subjects',
    'register',
    'login',
    'home',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'navigatte.urls'

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

WSGI_APPLICATION = 'navigatte.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#Database credentials populate
import dj_database_url

#If we are in production env
if "BLUEMIX_REGION" in os.environ:
    DATABASES = {'default': dj_database_url.config()}
else: #non production env
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
        #'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


#Static file directory inclusion
#If we are in production env
if "BLUEMIX_REGION" in os.environ:
    #Serve static files in the root static folder
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else: #non production env
    #Serve on correspondent static folders
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'static'),
    ]

STATIC_URL = '/static/'



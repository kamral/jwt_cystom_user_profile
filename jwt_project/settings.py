"""
Django settings for jwt_project project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# чтобы высчитывать разницу во времени
from datetime import  timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5=hcuba7pe_%6bn_((zio_7p%ioo#ab!m5x@g+6$-hr-9c4rh&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user',
    'profiles',
    'api'
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

ROOT_URLCONF = 'jwt_project.urls'

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

WSGI_APPLICATION = 'jwt_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'user_jwt',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'jwt_db_3'

    }
}

AUTH_USER_MODEL='user.User'
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

REST_FRAMEWORK={
# разрешение на уровне проекта
    'DEFAULT_PERMISSION_CLASSES':[
# разрешение для авторизованных
        'rest_framework.permissions.IsAuthenticated',
# разрешение для админа
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':(
# для выдачи json web token
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

# для определения настройки JWT
# JSONWebTojenAuthetication
JWT_AUTH={
# JWT_ENCODE_HANDLER: полезная нагрузка, которую мы хотим кодировать.

    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',
# JWT_PAYLOAD_HANDLER: данные, которые мы хотим передать как полезную нагрузку.
    'JWT_PAYLOAD_HANDLER':
    'rest_framework.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils_get_user_id_from_payload_handler',
# JWT_SECRET_KEY: секретный ключ для кодирования / декодирования токена
    'JWT_SECRET_KEY':'SECRET_KEY',
    'JWT_GET_USER_KEY':None,
    'JWT_PUBLIC_KEY':None,
    'JWT_PRIVATE_KEY':None,
# JWT_ALGORITHM: какой алгоритм использовать
    'JWT_ALGORITM':'HS256',
# JWT_VERIFY: если мы хотим проверить токен, всегда должно быть True
    'JWT_VERIFY':True,
# JWT_VERIFY_EXPIRATION: если срок действия токена истек.
    'JWT_VERIFY_EXPIRATION':True,
    'JWT_AUDIENCE':True,
    'JWT_ISSUER':None,
    'JWT_ALLOW_REFRESH':False,
# JWT_EXPIRATION_DELTA: время истечения срока действия токена, можно в минутах, часах, днях
    'JWT_REFRESH_EXPIRATION_DELTA':timedelta(days=30),
# JWT_AUTH_HEADER_PREFIX: префикс, который будет использоваться с токеном,
    # как правило, мы предпочитаем Bearer
    'JWT_AUTH_HEADER_PREFIX':'Bearer',
    'JWT_AUTH_COOKIE':None


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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

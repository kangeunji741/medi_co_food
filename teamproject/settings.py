"""
Django settings for teamproject project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2u7ri$d*hbp9jul=+fpf(x)d7p7tia)2p^eadr1i)!!s67v6op"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "board",
    "my",
    "allauth",  # pip install django-allauth 이용하여 소셜 로그인 기능 이용 시 아래 3개의 앱 작성
    "best",
    "product",
    "allauth.account",  # 2번
    "allauth.socialaccount",  # 3번
    "allauth.socialaccount.providers.naver",  # admin페이지 내에 강은지 관리자키 발급해 놓음
    "allauth.socialaccount.providers.kakao",
    "django.contrib.humanize",
    # "allauth.socialaccount.providers.google", 구글은 넣을까요 말까요,..? 구글은 대부분 프로필이나 나이 설정이 적어서
    # 타 사이트 들과 매칭되는 정보가 적습니다.


]
#  아래 AUTHENTICATION_BACKENDS도 소셜 어카운트 기능을 사용하기 위해 백엔드에 auth 모델을 추가 하는 것
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
#  이것 또한 공식 api 문서에서 요구하는 내용, 공식 api문서란 카카오맵 사용 시 디벨로퍼 페이지에서 꼭 작성하라고 했던 것들을 말함.
SITE_ID = 1  # 기본 사이트 ID 설정

SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True

LOGIN_REDIRECT_URL = "/main"  # 로그인 완료 시, 넘어갈 url주소 설정(로컬 주소 임.)
ACCOUNT_LOGOUT_REDIRECT_URL = '/main/login'  # 로그아웃 후 리디렉션 할 페이지


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
     # 추가할 미들웨어
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = "teamproject.urls"

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "teamproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {

    }
}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# https://velog.io/@aboutjoo/django-drf%EC%99%80-simplejwt-package
# 소셜로그인 한 유저들이 작성한 글이나 정보를 저장하기 위해 추후 위 블로그를 참고하여 아래코드를 활용해야 함,
# JWT SETTINGS

REST_USE_JWT = True

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

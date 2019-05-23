"""
Django settings for bipad project.
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from psycopg2cffi import compat
from django.utils.translation import ugettext_lazy as _

compat.register()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    '*q0n!x1vop1)mt2go)qf6*7)^69l)!&pr%(k)*g@_f$*n5@dw-'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = [os.environ.get('SERVER_ALLOWED_HOST', '*')]


# Application definition

INSTALLED_APPS = [
    'polymorphic',

    'jet.dashboard',
    'jet',
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_pgviews',   

    'autofixture',
    'corsheaders',
    'silk',
    'drf_yasg',
    'colorfield',
    'mptt',

    'django_celery_beat',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'django_select2',
    'mapwidgets',
    'reversion',

    'alert',
    'hazard',
    'incident',
    'event',
    'loss',
    'organization',
    'federal',
    'resources',
    'inventory',
    'realtime',
    'misc',
    'document',
    'relief',
    'user',
    'risk_profile',


]

MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bipad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bipad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DATABASE_NAME', 'postgres'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 1000,
    'HTML_SELECT_CUTOFF': 20,
}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "bipad/static"),
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Celery
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TIMEZONE = TIME_ZONE

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

JET_DEFAULT_THEME = 'default'
JET_SIDE_MENU_COMPACT = True
JET_INDEX_DASHBOARD = 'bipad.dashboard.IndexDashboard'

# DJANGO SILK
SILKY_META = True
SILKY_AUTHENTICATION = True
SILKY_AUTHORISATION = True
SILKY_MAX_RESPONSE_BODY_SIZE = 1024*100  # bytes
SILKY_INTERCEPT_PERCENT = int(os.environ.get('DJANGO_SILKY_INTERCEPT_PERCENT', '0'))


def SILKY_PERMISSIONS(user): return user.is_superuser


SILKY_MAX_RESPONSE_BODY_SIZE = 1024*100  # bytes
SILKY_INTERCEPT_PERCENT = int(os.environ.get('DJANGO_SILKY_INTERCEPT_PERCENT', '0'))

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 6),
        ("markerFitZoom", 12),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'np', }}),
    ),
    "GOOGLE_MAP_API_KEY": os.environ.get('GOOGLE_MAPS_API_KEY'),
    "LANGUAGE": "ne",
}

FEDERAL_CACHE_CONTROL_MAX_AGE = 60*60*24*7


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': 60 * 60 * 24,
    }
}
SELECT2_CACHE_BACKEND = 'select2'

# SENTRY
sentry_sdk.init(
    dsn=os.environ.get("DJANGO_SENTRY_DSN"),
    integrations=[DjangoIntegration()]
)

DATA_UPLOAD_MAX_NUMBER_FIELDS = int(os.environ.get('DJANGO_DATA_UPLOAD_MAX_NUMBER_FIELDS', '1000'))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


SESSION_COOKIE_HTTPONLY = False


def gettext(s): return s


LANGUAGES = (
    ('en', _('English')),
    ('ne', _('Nepali')),
)

DEFAULT_FROM_EMAIL = 'bipad@moha.gov.np'
SERVER_EMAIL = 'bipad@moha.gov.np'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.moha.gov.np'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bipad@moha.gov.np'
EMAIL_HOST_PASSWORD = 'B!p@d#468'
SERIALIZATION_MODULES = {
    "custom_geojson": "risk_profile.geojson_serializer",
}

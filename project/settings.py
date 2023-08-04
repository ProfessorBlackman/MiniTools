import os
from datetime import timedelta
from pathlib import Path
from decouple import config
from logging import FileHandler
from django.utils.log import ServerFormatter

from utils.logging.custom_logging import DefaultJsonFormatter, DetailedJsonFormatter

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]
if config("DEBUG", default=False, cast=bool):
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #     Third-party apps
    'drf_yasg',
    'rest_framework',
    'corsheaders',
    'django_extensions',
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    'silk',
    'django_celery_beat',
    'django_celery_results',

    #     Custom apps
    'apps.Users.apps.UsersConfig',
    'apps.BitLink.apps.BitlinkConfig',
    'apps.logging_app.apps.LoggingAppConfig',

    # Monitoring App
    "django_prometheus",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.middleware.gzip.GZipMiddleware",
    'silk.middleware.SilkyMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

PASSWORD_RESET_TIMEOUT = 1800

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'Users.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configurations
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "exceptions.exceptionHandler.custom_exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=8),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=4),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
}

# celery configurations
CELERY_CONFIG_MODULE = 'project.celeryconfig'
CELERY_BROKER_URL = config("CELERY_BROKER_URL")

# Redis configuration
REDIS_CONFIG = {
    "host": config("REDIS_HOST_URL"),
    "port": config("REDIS_PORT", default=6379, cast=int),
    "db": 0,
}

# Logging configuration

LOG_FILES_DIR = BASE_DIR / "logs"


def create_path(file_name: str):
    return LOG_FILES_DIR / file_name


log_files = {
    "redis_logger": create_path("redis_logs.log"),
    "tasks_info_log": create_path("tasks_info.log"),
    "tasks_warnings_log": create_path("tasks_warnings.log"),
    "tasks_errors_log": create_path("tasks_errors.log"),
    "tasks_critical_log": create_path("tasks_critical.log"),
    "worker_info_log": create_path("worker_info.log"),
    "website_info_log": create_path("websites_scraped.log"),
    "mini": create_path("minitools.log"),
    "database": create_path("database.log")
}

for file_path in log_files.values():
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

file_handlers = FileHandler

# Logging was here

FRONTEND_DOMAIN = config("FRONTEND_DOMAIN")

# silk config
SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
SILKY_PYTHON_PROFILER_RESULT_PATH = '/profiles'
SILKY_PYTHON_PROFILER_EXTENDED_FILE_NAME = True

# django cache config
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

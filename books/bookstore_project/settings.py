import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get("ENVIRONMENT", default="development")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    "crispy_forms",
    "allauth",
    "allauth.account",
    "debug_toolbar",
    # local
    "users.apps.UsersConfig",
    "pages.apps.PagesConfig",
    "books.apps.BooksConfig",
    "orders.apps.OrdersConfig",
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ""

ROOT_URLCONF = "bookstore_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "bookstore_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# URL that we can use to use to reference static files
STATIC_URL = "/static/"

# static directory - local environment
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# static directory - production environment
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # new


# tells Django how to look for static file directories - optional

# The FileSystemFinder looks within the STATICFILES_DIRS setting, which we set to
# static, for any static files.

# Then the AppDirectoriesFinder looks for any directories
# named static located within an app
"""
This setting is read top-to-bottom meaning if a file called static/img.jpg
is first found by FileSystemFinder it will be in place of an img.jpg file located within,
say, the pages app at pages/static/img.jpg.
"""

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# custom user model
AUTH_USER_MODEL = "users.CustomUser"

# Redirect user to homepage after login/logout
LOGIN_REDIRECT_URL = "home"

# django-allauth config
ACCOUNT_LOGOUT_REDIRECT = "home"
# LOGOUT_REDIRECT_URL = "home"

# django-crispy-forms
CRISPY_TEMPLATE_PACK = "bootstrap4"


# django-allauth config
SITE_ID = 1  # new
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False  # new
ACCOUNT_AUTHENTICATION_METHOD = "email"  # new
ACCOUNT_EMAIL_REQUIRED = True  # new
ACCOUNT_UNIQUE_EMAIL = True  # new


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "admin@djangobookstore.com"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Stripe
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get("STRIPE_TEST_PUBLISHABLE_KEY")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY")


# django-debug-toolbar
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


# production
if ENVIRONMENT == "production":
    SECURE_BROWSER_XSS_FILTER = True # javascript embeded
    X_FRAME_OPTIONS = 'DENY' # Clickjacking Protection
    SECURE_SSL_REDIRECT = True # HTTPS
    SECURE_HSTS_SECONDS = 3600 # new
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
    SECURE_HSTS_PRELOAD = True # new
    SECURE_CONTENT_TYPE_NOSNIFF = True # new
    SESSION_COOKIE_SECURE = True # new
    CSRF_COOKIE_SECURE = True # new


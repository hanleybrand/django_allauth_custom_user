"""
Django settings for django_allauth_custom_user project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging
# from userdata.models import CtrackUser

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../'))
CONFIG_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'media'))
MEDIA_URL = '/userfiles/'

STATIC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # TODO: remove dev only dirs when deployed
    os.path.normpath(os.path.join(PROJECT_ROOT, 'custom_user', 'static')),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


INSTALLED_APPS = (
    # The Django sites framework is required
    'django_trace',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'custom_user',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'thisisaterriblesecretkeythatyoushouldchangeassoonasyougetaroundtoit'

FACEBOOK_APP_ID = 'xxxxxxxxx'
FACEBOOK_APP_SECRET = 'xxxxxxxxxxxx'

#AUTH_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = 'custom_user.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_ADAPTER = 'custom_user.adaptor.AccountAdapter'
ACCOUNT_SIGNUP_FORM_CLASS = 'custom_user.forms.SignupForm'
LOGIN_REDIRECT_URL = '/profile'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email',
                  'publish_stream'],
        #'first_name', 'last_name',
        #'birthday',
        #'age_range', 'gender'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}

GENDER_CHOICES = (('', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other'),)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # allauth specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(PROJECT_ROOT, 'templates')),
    os.path.normpath(os.path.join(PROJECT_ROOT, 'custom_user', 'templates')),
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_allauth_custom_user.urls'

WSGI_APPLICATION = 'django_allauth_custom_user.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


DEBUG_TOOLBAR_PATCH_SETTINGS = True

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = (
    {
        #'INTERCEPT_REDIRECTS': False,
        'RENDER_PANELS': True,
        #'SHOW_TOOLBAR_CALLBACK' : 'config.settings.show_toolbar'
    }
)
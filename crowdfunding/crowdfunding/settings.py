import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ("crowdf", "crowdf@mailinator.com"),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.postgresql_psycopg2",
        "NAME" : "together",
        "USER" : "together_user",
        "PASSWORD" : "together_password",
        "HOST" : "",
        "PORT" : ""
    }
}

ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'America/Santiago'

LANGUAGE_CODE = 'es-CL'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = "/home/crowdf/webapps/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = "/home/crowdf/webapps/static/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.join(SITE_ROOT,os.pardir), "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'egb2(g$8qr(2ofz3dqt*kyyhth)^&8^fq)9dshhhm5$#2gvxoe'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crowdfunding.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crowdfunding.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'south',
    'together',
    'social_auth',
)

#configuracion social_auth.
#TO-DO : 
# - validar app id y api secret, datos tomados desde js
# - Tengo mis dudas sobre la Url login.
# - Crear login_error_url

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social_auth.context_processors.social_auth_by_type_backends',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook')
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

#Fuertes dudas.
FACEBOOK_APP_ID              = '1420749211490800'
FACEBOOK_API_SECRET          = '32f8fcbfa167f64d3ee072d9b586a503'

LOGIN_URL = '/fb_login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "rlaysystems@gmail.com"
EMAIL_HOST_PASSWORD = "realreyes"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

try:
    from .local_settings import *
except ImportError:
    pass

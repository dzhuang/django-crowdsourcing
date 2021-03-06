# Django settings for example_app project.
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DATABASE_ENGINE = 'django.db.backends.sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')


"""
Follow these directions to build the documentation using Sphinx. Then the
example app will serve the documentation.

1. Install Sphinx. For example,
   $ pip install sphinx
2. Build the documentation using Sphinx.
   $ cd django-crowdsourcing/docs
   $ sphinx-build -b html . _build
"""
DOCUMENTATION_ROOT = os.path.join(PROJECT_ROOT, '../docs/_build')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%n@##5o0%d@qd5l4^+(zt5ih@90a7ch4k3m7a^!5unw45)i=ly'

from django.conf.global_settings import STATICFILES_FINDERS

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = 'example_app.urls'


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": (
            os.path.join(PROJECT_ROOT, 'example_app', "templates"),
            ),
        "OPTIONS": {
            "context_processors": (
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                ),
            "debug": DEBUG
            },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    "djangobower",
    'crowdsourcing',
    'cms',
)


BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, "components")

STATICFILES_FINDERS = tuple(STATICFILES_FINDERS) + (
    "djangobower.finders.BowerFinder",
    )

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap#3.3.7',
    'jquery-form',
    'jcarousel',
    'bootstrap-datepicker',

    # bower installed but failed yui
    #'yui3'
)



STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'example_app', "static"),
        )

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

try:
    from local_settings import *
except ImportError:
    pass



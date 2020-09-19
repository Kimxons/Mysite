"""
Django settings for Mysite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cofti!t@g0$ws6f%7(czj$k1!trpc3pz=z8+jf3pk!gwfcbex!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #my apps
    'main',
    'blog',
    'projects',
]

JAZZMIN_SETTINGS = {
    #window title
    'site_title': 'Meshack Kimwele',
    #brand title, & login screen(19 chars max)
    'site_header': 'Meshack Kimwele',
    #welcome text on login screen
    'welcome_sign': 'Welcome to Meshak Kimwele',
    #copyright at footer
    'copyright': 'Meshack Kimwele',
    #The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'auth.User',
    #field name on user model that contain an avatar
    'user_avatar': None,

    # Top menu
    # links in the top menu

    #url that gets reversed - admin_homepage
    'topmenu_links': [
        {'name': 'Home', 'url': 'admin.index', 'permissions':['auth.View_user']},
        #url that retrieves pages
        {'name': 'Pages', 'url': ''},
        {'name': 'Blog', 'url': ''},
        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},

        # url to visit the site 
        {'name': 'View Site','url': ''}, #Remember to include the link
    ],

        ##side menu
        # Whether to display the side menu
        'show_sidebar': True,

        # Whether to aut expand the menu
        'navigation_expanded': True,

        # Hide these apps when generating side menu e.g (auth)
        'hide_apps': [],

        # Hide these models when generating side menu (e.g auth.user)
        'hide_models': [],

        # List of apps to base side menu ordering off of (does not need to contain all apps)
        'order_with_respect_to': ['accounts', 'polls'],

        # Custom links to append to app groups, keyed on app name
        'custom_links': {
            'polls': [{
                'name': 'Make Messages', 
                'url': 'make_messages', 
                'icon': 'fas fa-comments',
                'permissions': ['polls.view_poll']
            }]
        },

        # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
        # for a list of icon classes
        'icons': {
            'auth': 'fas fa-users-cog',
            'auth.user': 'fas fa-user',
            'auth.Group': 'fas fa-users',
        },
        # Icons that are used when one is not manually specified
        'default_icon_parents': 'fas fa-chevron-circle-right',
        'default_icon_children': 'fas fa-circle',

        #############
        # UI Tweaks #
        #############
        # Relative paths to custom CSS/JS scripts (must be present in static files)
        "custom_css": None,
        "custom_js": None,
        # Whether to show the UI customizer on the sidebar
        "show_ui_builder": False,

        ###############
        # Change view #
        ###############
        # Render out the change view as a single form, or in tabs, current options are
        # - single
        # - horizontal_tabs (default)
        # - vertical_tabs
        # - collapsible
        # - carousel
        "changeform_format": "horizontal_tabs",
        # override change forms on a per modeladmin basis
        "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Mysite.urls'

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

WSGI_APPLICATION = 'Mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# -*- encoding: utf-8 -*-


import os
from decouple import config
from unipath import Path
from socket import gethostname, gethostbyname
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = Path(__file__).parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
################### Production #####################
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'xdguhdfxuyktgdfiughdghbghhfhfgh$$$&&33nn3n3n3d&&8888***')
################### XXXXX #####################


################### Local Run #####################
# SECRET_KEY = config('SECRET_KEY')
################### XXXXX #####################
# SECURITY WARNING: don't run with debug turned on in production!
################### Production #####################
# DEBUG = bool(int(os.environ.get('DEBUG',0)))
################### XXXXX #####################

################### Local #####################
DEBUG = config('DEBUG', default=True, cast=bool)
################### XXxxx      #####################

# load production server from .env
ALLOWED_HOSTS = ['127.0.0.1', config('SERVER', default='127.0.0.1')]


ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(',')
    )
)
if os.environ.get('AWS_EXECUTION_ENV'):
    ALLOWED_HOSTS.append(gethostbyname(gethostname()))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    # 'mytaxboard_api',
    'rest_framework',
    'drf_yasg',
    'rest_framework_swagger',
    'account',  # change this
    'business',
    'home',
    'channels',
    'django_celery_beat',
    'django_celery_results',
    'notifications_app',
    'storages',  
    'django_social_share',


    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'crispy_forms',
    # 'blog',
    'home_wagtail',
    # 'search',
    'wagtail.contrib.settings',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'ckeditor',
  
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware'
]



ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "/account/login_success"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "core/templates")  # ROOT dir for templates
# LOGIN_URL = 'account/facebook/login/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        # 'DIRS': [TEMPLATE_DIR,os.path.join(BASE_DIR, "templates"),os.path.join(BASE_DIR, "home_wagtail/templates"),os.path.join(BASE_DIR, "blog/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.custom_context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'


####################### Production ##############

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'HOST': os.environ.get('DB_HOST'),
#     'NAME': os.environ.get('DB_NAME'),
#     'USER': os.environ.get('DB_USER'),
#     'PASSWORD': os.environ.get('DB_PASS'),
#     }
# }

############# xxx ##############################


############ Local Run #########################

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }

    }
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

############# xxx ##############################

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

WAGTAIL_SITE_NAME = 'core'

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
###### Using Local Run ##############
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT  = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


######## End #############

# USE_S3 ='TRUE'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_STORAGE_BUCKET_NAME')
# AWS_DEFAULT_ACL = 'private'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# PRIVATE_MEDIA_LOCATION = 'private'
# PRIVATE_FILE_STORAGE = 'core.storage_backends.PrivateMediaStorage'
# AWS_S3_REGION_NAME =('ap-south-1')

# PUBLIC_MEDIA_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'

# ############ Using production #########
# ####### Volume 
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'

# MEDIA_ROOT = '/vol/web/media'
# STATIC_ROOT = '/vol/web/static'
 
 ############## End ##############
# AUTH_USER_MODEL = 'core.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'arun887126@gmail.com'
EMAIL_HOST_PASSWORD = 'hrqycglzdaftfskl'
EMAIL_USE_SSL = True
# EMAIL_USE_SSL = True

 #############################################################
#############################################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 8000)],
        },
    },
}

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://127.0.0.1:8000'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SELERLIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

######################################################
###################Paytm##############################

PAYTM_PAYMENT_GATEWAY_URL = "https://securegw-stage.paytm.in/order/process"
PAYTM_TRANSACTION_STATUS_URL = "https://securegw-stage.paytm.in/order/status"

# Start Used For Staging 
PAYTM_MERCHANT_ID = 'swZnNU29275414462961'
PAYTM_SECRET_KEY = 'eY_9DO8EGHqxKbQ_'
PAYTM_WEBSITE = 'WEBSTAGING'
# End Used For Staging 


# Start Used For Production 
# PAYTM_MERCHANT_ID = os.environ.get('PAYTM_MERCHANT_ID')
# PAYTM_SECRET_KEY = os.environ.get('PAYTM_SECRET_KEY')
# PAYTM_WEBSITE = 'DEFAULT'
# End Used For Production 

# PAYTM_CHANNEL_ID = 'WEB'
# PAYTM_INDUSTRY_TYPE_ID = 'Retail'


########################END Paytm########################
#########################################################



# HTTPS settings
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
#  HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


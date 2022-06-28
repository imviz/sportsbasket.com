"""
Django settings for sportsbasket project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from email.policy import default
from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =config('DEBUG' , cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'category',
    'products',
    'orders',
    'adminz',
    'storages',
    
   
 
    
   
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

ROOT_URLCONF = 'sportsbasket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',                
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #slug linkss
                'products.context_processors.menu_links',
                'products.context_processors.submenu_links',
                'products.context_processors.counter',
                
               
              
            ],
        },
    },
]

WSGI_APPLICATION = 'sportsbasket.wsgi.application'
#for model
AUTH_USER_MODEL='user.Account'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB_NAME',cast=str),
        'USER': config('DB_USER',cast=str),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'), 
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# STATIC_URL = '/static/'
# STATIC_ROOT = '/staticfiles '
# STATICFILES_DIRS = [
#     os.path.join( BASE_DIR / "static")
#  ]

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400',
}
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIRS=[
    'static',
]
STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'sportsbasket.media_storages.MediaStorage'



#media file confirmation email
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT= config('EMAIL_PORT' ,cast=int)
EMAIL_HOST_USER =config('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD') 
# EMAIL_HOST_USER ='vishnuedappatt@gmail.com'
# EMAIL_HOST_PASSWORD='Epunhsiv'

EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool,)




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_ROOT =BASE_DIR / 'media'
MEDIA_URL  = '/media/'
	
LOGIN_URL = '/login/'

TWILIO_VERIFY_SERVICE_SID=config('TWILIO_VERIFY_SERVICE_SID')
TWILIO_ACCOUNT_SID= config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN= config('TWILIO_AUTH_TOKEN') 

# captcha viewing
GOOGLE_RECAPTCHA_SECRET_KEY =config('GOOGLE_RECAPTCHA_SECRET_KEY')

# payment
RAZORPAY_ID=config('RAZORPAY_ID')
RAZORPAY_KEY=config ('RAZORPAY_KEY')




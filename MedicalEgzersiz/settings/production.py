from MedicalEgzersiz.settings.base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fitnessmonitor_db',
        'USER': 'fitness_user',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '',

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
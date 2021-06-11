from .settings import BASE_DIR , env
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
localhost = True if env('LOCALHOST') == 'True' else False
if localhost:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else :
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
    }
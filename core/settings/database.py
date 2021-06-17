from .settings import BASE_DIR , env
import dj_database_url
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
    #heroku
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }
    # db_from_env = dj_database_url.config(conn_max_age=600)
    # DATABASES['default'].update(db_from_env)
    #Local use
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  env('NAME'),
        'USER':  env('USER'),
        'PASSWORD':  env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT':  env('PORT'),
    }
    }
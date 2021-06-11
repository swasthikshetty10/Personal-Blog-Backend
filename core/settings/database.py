from .settings import BASE_DIR , env
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
localhost = True if env('localhost') == 'True' else False
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

        'ENGINE': env('ENGINE'),

        'NAME':  env('NAME'),

        'USER':  env('USER'),

        'PASSWORD':  env('PASSWORD'),

        'HOST': env('HOST'),

        'PORT':  env('PORT'),

    }
    }
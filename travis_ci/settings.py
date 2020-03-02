from Madswan.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'madswan',
        'USER': 'travis',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

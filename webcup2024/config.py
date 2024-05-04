import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR /'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'

SECRET_KEY = 'django-insecure-xg_zqjgikxw&@#!(&660=p@1(x&)n9wr5*+)#bq&2cc$darbjt'

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')
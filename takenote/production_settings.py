from pathlib import Path
import os
from decouple import config # altered for production

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = config('SECRET_KEY')  # altered for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # altered for production

ALLOWED_HOSTS = ['takenote-lhckb.herokuapp.com'] # altered for production


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')


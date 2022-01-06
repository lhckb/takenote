
from pathlib import Path
import os
from decouple import config # altered for production


SECRET_KEY = config('SECRET_KEY')  # altered for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # altered for production

ALLOWED_HOSTS = ['*'] # altered for production


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


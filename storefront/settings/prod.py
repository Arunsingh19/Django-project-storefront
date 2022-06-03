import os
import psycopg2 as Database
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['arunsingh-prod.herokuapp.com']

DATABASES = {
    'default' : dj_database_url.config()
}


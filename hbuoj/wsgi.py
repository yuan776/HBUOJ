import os

from django.core.wsgi import get_wsgi_application
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hbuoj.settings')

try:
    import MySQLdb
except ImportError:
    import pymysql

    pymysql.install_as_MySQLdb()

application = Sentry(get_wsgi_application())
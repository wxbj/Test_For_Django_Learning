import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test_For_Django_Learning.settings')

application = get_wsgi_application()

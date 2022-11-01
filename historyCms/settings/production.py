from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "historyCms.urls"
SECRET_KEY = "django-insecure-0(%wg9!8s&+t3ew+)^n-w+*7fyyg=#+u#n9k-!_cs3ofvhf5l4"
try:
    from .local import *
except ImportError:
    pass

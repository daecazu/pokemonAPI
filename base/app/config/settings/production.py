"""Production settings."""

from .base import *  # NOQA
from .base import env

# Base
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['localhost'])


#CORS_ORIGIN_WHITELIST = ['http://eborastester.detektorgps.com',]

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
} 

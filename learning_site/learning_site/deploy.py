"""
WSGI config for learning_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

path = = "/home/brianweber2/deploying_django/learning_site/learning_site"
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_site.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

"""
WSGI config for zine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zine.settings")

# add the hellodjango project path into the sys.path
sys.path.append('/Users/gabrielleharrison/Desktop/git/zine')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/Users/gabrielleharrison/virtualenvs/virtualenv_zine/Lib/site-packages')

application = get_wsgi_application()

import os
import sys

path = '/home/cslansing/vexxesports/vexxesports'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'vexxesports.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

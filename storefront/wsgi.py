"""
WSGI config for storefront project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from app import app
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

application = get_wsgi_application()

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 400))
  app.run(host="0.0.0.0", port=port)

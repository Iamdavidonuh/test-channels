import os

import django
from channels.routing import get_default_application

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testsite.settings')

django.setup()


from channels.auth import AuthMiddlewareStack
import testsite.routing




application = ProtocolTypeRouter({
    #'http': AsgiHandler(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            testsite.routing.websocket_urlpatterns
        )
    ),
})
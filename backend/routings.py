from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from backend.tasks.consumers import NotificationConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/notifications/', NotificationConsumer.as_asgi()),
    ])
})

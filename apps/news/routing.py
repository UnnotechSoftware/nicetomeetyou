from django.urls import path

from apps.news import consumers


urlpatterns = [
    path('ws/task_status/', consumers.NotificationConsumer.as_asgi()),
]
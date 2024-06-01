from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


def send_notification():
    async_to_sync(channel_layer.group_send)(
        "notification_group",
        {
            "type": "notification.message",
            "message": "You got a new news!!"
        }
    )

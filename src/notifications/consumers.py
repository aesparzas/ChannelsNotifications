from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class NotificationConsumer(JsonWebsocketConsumer):

    def connect(self):
        super().connect()
        async_to_sync(self.channel_layer.group_add)('notifications_group',
                                                    self.channel_name)

    def send_notification(self, notification):
        if isinstance(notification, dict):
            notification = notification['notification']
        json = {
            "type": "notification",
            "content": {
                "id": notification.pk,
                "header": notification.header,
                "body": notification.text,
            },
        }
        self.send_json(json)

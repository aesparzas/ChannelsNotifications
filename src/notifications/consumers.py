from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from notifications.models import Notification


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

    def send_must_refresh(self):
        json = {
            "type": "mustRefresh",
            "content": {},
        }
        self.send_json(json)

    def receive_json(self, content, **kwargs):
        if content['type'] == 'read':
            id = content['content']['id']
            notification = Notification.objects.get(pk=id)
            notification.is_read = True
            notification.save()
            self.send_must_refresh()

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.utils import timezone


class Notification(models.Model):
    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    header = models.CharField('header', max_length=56)
    text = models.CharField('text', max_length=256)
    datetime = models.DateTimeField('datetime', editable=False,
                                    default=timezone.now)
    is_read = models.BooleanField('is it already read?', default=False)

    def __str__(self):
        return f"{self.header} ({str(self.datetime.isoformat())})"

    def save(self, **kwargs):
        if not self.pk:
            super().save(**kwargs)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'notifications_group',
                {'type': 'send_notification', 'notification': self}
            )
        else:
            super().save(**kwargs)
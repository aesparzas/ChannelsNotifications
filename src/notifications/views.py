from django.shortcuts import render
from django.views.generic import TemplateView


__all__ = ['IndexView']

from notifications.models import Notification


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notifications = Notification.objects.all().order_by('-datetime')[:8]
        new_notifications = Notification.objects.filter(is_read=False).count()
        context['notifications'] = notifications
        context['new_notifications'] = new_notifications
        return context

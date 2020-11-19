from django.shortcuts import render
from django.views.generic import TemplateView


__all__ = ['IndexView']


class IndexView(TemplateView):
    template_name = 'index.html'

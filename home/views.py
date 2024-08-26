from django.shortcuts import render
from django.views.generic import TemplateView


"""
Resusable view to render a template or display a static page
"""
class HomeTemplateView(TemplateView):
    template_name = "home/index.html"
from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "home/index.html"


class AboutUsView(TemplateView):
    template_name = "home/about.html"
"""
URL configuration for the Home app.
"""

from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="index"),
    path("about/", views.HomeTemplateView.as_view(template_name="home/about.html"), name="about"),
    path("pachito&chipie/", views.HomeTemplateView.as_view(template_name="home/pachito&chipie.html"), name="easter-egg"),
]
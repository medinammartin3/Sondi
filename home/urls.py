from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.HomepageView.as_view(), name="index"),
    path("about/", views.AboutUsView.as_view(), name="about")
]
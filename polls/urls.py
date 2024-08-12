from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("results/<int:pk>/", views.ResultsView.as_view(), name="results"),
    path("vote/<int:question_id>", views.vote, name="vote"),
    path("create", views.CreatePollView.as_view(), name="create"),
    path("confirmation/<int:pk>/", views.ConfirmationView.as_view(), name="confirmation"),
]
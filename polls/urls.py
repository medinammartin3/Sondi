"""
URL configuration for the Polls app.
"""

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vote/results/<str:encoded_id>/", views.ResultsView.as_view(), name="results"),
    path("vote/<str:question_code>/", views.vote, name="vote"),
    path("create/", views.CreatePollView.as_view(), name="create"),
    path("create/confirmation/<str:encoded_id>/", views.ConfirmationView.as_view(), name="confirmation"),
    path("mypolls/", views.UserPollsView.as_view(), name="user_polls"),
    path("results/<str:encoded_id>/", views.OwnerResultsView.as_view(), name="owner_results"),
]
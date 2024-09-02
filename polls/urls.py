"""
URL configuration for the Polls app.
"""

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vote/results/<int:pk>/", views.ResultsView.as_view(), name="results"),
    path("vote/<str:question_code>/", views.vote, name="vote"),
    path("create/", views.CreatePollView.as_view(), name="create"),
    path("confirmation/<int:pk>/", views.ConfirmationView.as_view(), name="confirmation"),
    path("mypolls/", views.UserPollsView.as_view(), name="user_polls"),
    path("results/<int:pk>/", views.OwnerResultsView.as_view(), name="owner_results"),
]
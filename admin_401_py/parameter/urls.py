from django.urls import path

from . import views

urlpatterns = [
    # ex: /parameter/
    path("", views.index, name="index"),
    # ex: /parameter/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /parameter/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /parameter/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
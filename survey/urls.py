from django.urls import path

from .views import *

urlpatterns = [
    path("", SurveyView.as_view(), name="survey"),
    path("complete/", SurveyViewComplete.as_view(), name="survey_complete"),
]

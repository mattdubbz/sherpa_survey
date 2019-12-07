from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy

from .models import Survey
from .forms import SurveyForm

# Create your views here.
class SurveyView(TemplateView):
    model = Survey
    form = SurveyForm
    template_name = "survey.html"
    success_url = reverse_lazy("survey_complete.html")


class SurveyComplete(TemplateView):
    template_name = "survey_complete.html"

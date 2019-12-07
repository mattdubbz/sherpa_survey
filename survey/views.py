from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .models import Survey
from .forms import SurveyForm

# Create your views here.
class SurveyView(FormView):
    model = Survey
    form = SurveyForm
    form_class = SurveyForm
    template_name = "survey.html"
    success_url = reverse_lazy("survey_complete")


class SurveyComplete(TemplateView):
    template_name = "survey_complete.html"

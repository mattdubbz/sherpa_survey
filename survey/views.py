from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .models import CustomerSatisfactionSurvey
from .forms import CustomerSatisfactionSurveyForm

# Create your views here.


class SurveyView(FormView):
    form_class = CustomerSatisfactionSurveyForm
    template_name = "survey.html"
    success_url = reverse_lazy("survey_complete")


class SurveyViewComplete(TemplateView):
    template_name = "survey_complete.html"

from django.forms import ModelForm

from .models import *


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"

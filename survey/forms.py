from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect

from .models import *


class SurveyForm(ModelForm):
    room_score1 = forms.IntegerField(label="How would you rate the amenities?")
    room_score2 = forms.IntegerField(label="How would you rate the activities?")
    room_score3 = forms.IntegerField(label="How would you rate the room?")
    room_score4 = forms.IntegerField(label="How would you rate the staff?")
    room_score5 = forms.IntegerField(
        label="How would you rate your overall experience?"
    )

    class Meta:
        model = Survey
        fields = "__all__"

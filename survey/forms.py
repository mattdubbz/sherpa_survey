from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect, Select

from .models import *


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"
        labels = {
            "room_score1": "How would you rate the amenities?",
            "room_score2": "How would you rate the activities?",
            "room_score3": "How would you rate the room?",
            "room_score4": "How would you rate the staff?",
            "room_score5": "How would you rate your overall experience?",
        }
        widgets = {
            "room_score1": Select,
            "room_score2": Select,
            "room_score3": Select,
            "room_score4": Select,
            "room_score5": Select,
        }

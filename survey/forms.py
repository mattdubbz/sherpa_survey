from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect, Select

from .models import *


class CustomerSatisfactionSurveyForm(ModelForm):
    class Meta:
        model = CustomerSatisfactionSurvey
        fields = '__all__'
        labels = {
            'amenities_score': 'How would you rate the amenities?',
            'activities_score': 'How would rate the activities?',
            'room_score': 'How would you rate the room?',
            'atmosphere_score': 'How would you rate the general atmosphere?',
            'staff_score': 'How would you rate the staff?',
            'service_score': 'How would you rate the overall service?',
            'overall_score': 'How would you rate your overall experience?',
            'improve_text': 'Is there any way that we could improve any of our ratings?',
            'comments': 'Anything else you want to tell us?'
        }
        widgets = {
            'amenities_score': Select,
            'activities_score': Select,
            'room_score': Select,
            'atmosphere_score': Select,
            'staff_score': Select,
            'service_score': Select,
            'overall_score': Select,
        }

from django.db import models
from django.urls import reverse

# Create your models here.


class Survey(models.Model):
    title = models.CharField(max_length=100)
    question1 = models.CharField(max_length=255)
    response1 = models.IntegerField(blank=False, null=False)
    question2 = models.CharField(max_length=255)
    response2 = models.IntegerField(blank=False, null=False)
    question3 = models.CharField(max_length=255)
    response3 = models.IntegerField(blank=False, null=False)
    question4 = models.CharField(max_length=255)
    response4 = models.IntegerField(blank=False, null=False)
    question5 = models.CharField(max_length=255)
    response5 = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("survey", args=[str(self.id)])

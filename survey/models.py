from django.db import models
from django.urls import reverse

# Create your models here.


class Survey(models.Model):
    room_score1 = models.IntegerField(blank=True, null=True)
    room_score2 = models.IntegerField(blank=True, null=True)
    room_score3 = models.IntegerField(blank=True, null=True)
    room_score4 = models.IntegerField(blank=True, null=True)
    room_score5 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("survey", args=[str(self.id)])

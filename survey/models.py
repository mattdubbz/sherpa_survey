from django.db import models
from django.urls import reverse


class Survey(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    SCORE_CHOICES = [(ONE, "1"), (TWO, "2"), (THREE, "3"), (FOUR, "4"), (FIVE, "5")]

    room_score1 = models.IntegerField(blank=True, null=True, choices=SCORE_CHOICES)
    room_score2 = models.IntegerField(blank=True, null=True, choices=SCORE_CHOICES)
    room_score3 = models.IntegerField(blank=True, null=True, choices=SCORE_CHOICES)
    room_score4 = models.IntegerField(blank=True, null=True, choices=SCORE_CHOICES)
    room_score5 = models.IntegerField(blank=True, null=True, choices=SCORE_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("survey", args=[str(self.id)])

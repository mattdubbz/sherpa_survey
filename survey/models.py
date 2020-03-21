from django.db import models
from django.urls import reverse


class CustomerSatisfactionSurvey(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    SCORE_CHOICES = [(ONE, '1'), (TWO, '2'), (THREE, '3'),
                     (FOUR, '4'), (FIVE, '5')]

    amenities_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    activities_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    room_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    atmosphere_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    staff_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    service_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    overall_score = models.IntegerField(
        blank=True, null=True, choices=SCORE_CHOICES)
    improve_text = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse("survey", args=[str(self.id)])

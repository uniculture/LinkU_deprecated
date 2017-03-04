from django.core.validators import RegexValidator
from django.db import models


class Meeting(models.Model):
    maker = models.TextField()
    name = models.TextField()
    place = models.TextField()
    start_time = models.DateTimeField()
    image_path = models.ImageField(blank=True)
    distance_near_univ = models.TextField()
    price_range = models.TextField()


class Applier(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.TextField(blank=False)
    phone_regex = RegexValidator(regex='^\d{11}$', message='Length has to be 11 & Only number')
    phone_number = models.CharField(blank=False, validators=[phone_regex], max_length=11)
    gender = models.CharField(blank=False, max_length=1, choices=GENDER_CHOICES)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)

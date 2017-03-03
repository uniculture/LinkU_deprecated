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
    name = models.TextField()
    phone_number = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)


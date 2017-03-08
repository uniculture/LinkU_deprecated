from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import RegexValidator


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


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    email = models.EmailField()
    nickname = models.TextField()
    profile = models.ImageField(blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13)
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

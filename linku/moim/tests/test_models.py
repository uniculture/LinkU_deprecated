from django.core.exceptions import ValidationError
from moim.models import Meeting, Applier, User
import datetime
import pytest


@pytest.mark.django_db
def test_save_applier():
    start_time = datetime.datetime.now()
    meeting = Meeting.objects.create(maker='test maker', name='test name', place='test place', start_time=start_time,
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    Applier.objects.create(name='test name', phone_number='01011111111', gender='M', meeting=meeting)


@pytest.mark.django_db
def test_save_meeting():
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    Meeting.objects.get(name='test name')


@pytest.mark.django_db
def test_cannot_save_empty_field_applier():
    meeting = Meeting.objects.create(maker='test maker', name='test name', place='test place', start_time=datetime.datetime.now(),
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    applier = Applier(name='', phone_number='', gender='', meeting=meeting)
    with pytest.raises(ValidationError):
        applier.save()
        applier.full_clean()


@pytest.mark.django_db
def test_cannot_save_wrong_format_phone_number_applier():
    meeting = Meeting.objects.create(maker='test maker', name='test name', place='test place', start_time=datetime.datetime.now(),
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    applier = Applier(name='test name', phone_number='010', gender='M', meeting=meeting)
    with pytest.raises(ValidationError):
        applier.save()
        applier.full_clean()

    applier2 = Applier(name='test name2', phone_number='010111122223', gender='M', meeting=meeting)
    with pytest.raises(ValidationError):
        applier2.save()
        applier2.full_clean()

    applier3 = Applier(name='test name3', phone_number='010aaaabbbb', gender='M', meeting=meeting)
    with pytest.raises(ValidationError):
        applier3.save()
        applier3.full_clean()


@pytest.mark.django_db
def test_save_user():
    User.objects.create(email='test email', password='test password', gender='M',
                        nickname='test nickname', phone_number='01024231412')
    User.objects.get(email='test email')

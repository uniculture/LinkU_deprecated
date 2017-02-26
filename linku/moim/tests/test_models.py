from moim.models import Meeting, Applier
import datetime
import pytest


@pytest.mark.django_db
def test_save_applier():
    start_time = datetime.datetime.now()
    meeting = Meeting.objects.create(maker='test maker', name='test name1', place='test place', start_time=start_time,
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')
    Applier.objects.create(name='test name', phone_number='010-1111-1111', gender='M', meeting=meeting)


@pytest.mark.django_db
def test_save_meeting():
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    Meeting.objects.get(name='test name')

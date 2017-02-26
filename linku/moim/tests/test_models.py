from moim.models import Meeting, Applier
import datetime
import pytest

def test_meeting_model_have_fields():
    Meeting._meta.get_field('maker')
    Meeting._meta.get_field('name')
    Meeting._meta.get_field('place')
    Meeting._meta.get_field('start_time')
    Meeting._meta.get_field('image_path')
    Meeting._meta.get_field('distance_near_univ')
    Meeting._meta.get_field('price_range')


def test_applier_model_have_fields():
    Applier._meta.get_field('name')
    Applier._meta.get_field('phone_number')
    Applier._meta.get_field('gender')
    Applier._meta.get_field('meeting')

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

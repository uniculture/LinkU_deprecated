import pytest
import datetime
from moim.models import Meeting


def test_meeting_model_have_fields():
    Meeting._meta.get_field('maker')
    Meeting._meta.get_field('name')
    Meeting._meta.get_field('place')
    Meeting._meta.get_field('start_time')
    Meeting._meta.get_field('image_path')
    Meeting._meta.get_field('distance_near_univ')
    Meeting._meta.get_field('price_range')


@pytest.mark.django_db
def test_save_meeting():
    Meeting.objects.create(maker='test', name='test', place='place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test', price_range='test')


@pytest.mark.django_db
def test_view_home(client):
    Meeting.objects.create(maker='test', name='돈까스 모임2', place='place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test', price_range='test')
    response = client.get('/')
    assert "돈까스 모임2" in response.content.decode("utf8")

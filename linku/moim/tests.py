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
def test_homepage_use_meeting_list_template(client):
    response_templates = client.get('/').templates
    assert 'meeting_list.html' in (
        template.name for template in response_templates)


@pytest.mark.django_db
def test_save_meeting():
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    Meeting.objects.get(name='test name')


@pytest.mark.django_db
def test_homepage_view_meeting_info(client):
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    response = client.get('/')
    assert "test name" in response.content.decode("utf8")

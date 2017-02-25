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
def test_apply_meeting_view_use_correct_template(client):
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    response_templates = client.get('/meetings/1/apply/').templates
    assert 'apply_meeting.html' in (
        template.name for template in response_templates)


@pytest.mark.django_db
def test_apply_meeting_view_return_correct_meeting_name(client):
    Meeting.objects.create(maker='test maker1', name='test name1', place='test place1',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ1', price_range='test price_range1')
    Meeting.objects.create(maker='test maker2', name='test name2', place='test place2',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ2', price_range='test price_range2')
    meeting = Meeting.objects.get(maker='test maker2')
    response = client.get('/meetings/' + str(meeting.id) + '/apply/')
    assert meeting.name in response.content.decode("utf8")


@pytest.mark.django_db
def test_save_meeting():
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=datetime.datetime.now(),
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    Meeting.objects.get(name='test name')


@pytest.mark.django_db
def test_homepage_view_meeting_info(client):
    start_time = datetime.datetime.now()
    Meeting.objects.create(maker='test maker', name='test name', place='test place',
                           start_time=start_time,
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    response = client.get('/')
    assert "test maker" in response.content.decode("utf8")
    assert "test name" in response.content.decode("utf8")
    assert "test place" in response.content.decode("utf8")
    assert "test distance_near_univ" in response.content.decode("utf8")
    assert "test price_range" in response.content.decode("utf8")

    # template가 포맷에 맞춰 반환하는지 테스트
    assert start_time.strftime(
        '%m/%d %H:%M') in response.content.decode("utf8")


@pytest.mark.django_db
def test_homepage_view_multiple_cards(client):
    start_time = datetime.datetime.now()
    Meeting.objects.create(maker='test maker', name='test name1', place='test place',
                           start_time=start_time,
                           distance_near_univ='test distance_near_univ', price_range='test price_range')
    Meeting.objects.create(maker='test maker', name='test name2', place='test place',
                           start_time=start_time,
                           distance_near_univ='test distance_near_univ', price_range='test price_range')

    response = client.get('/')
    assert "test name1" in response.content.decode("utf8")
    assert "test name2" in response.content.decode("utf8")

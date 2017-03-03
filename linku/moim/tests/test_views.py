import pytest
import datetime
from moim.models import Meeting, Applier, User


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


@pytest.mark.django_db
def test_save_applier_info_after_applying_post_request(client):
    start_time = datetime.datetime.now()
    meeting = Meeting.objects.create(maker='test maker', name='test name1', place='test place', start_time=start_time,
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')

    client.post('/meetings/%d/apply/' % (meeting.id,),
                data={'name': 'test name',
                      'phone_number': '010-1111-1111',
                      'gender': 'M'})
    Applier.objects.get(name='test name')


@pytest.mark.django_db
def test_redirect_to_homepage_after_applying_post_request(client):
    start_time = datetime.datetime.now()
    meeting = Meeting.objects.create(maker='test maker', name='test name1', place='test place', start_time=start_time,
                                     distance_near_univ='test distance_near_univ', price_range='test price_range')

    response = client.post('/meetings/%d/apply/' % (meeting.id,),
                           data={'name': 'test name',
                                 'phone_number': '010-1111-1111',
                                 'gender': 'M'})

    assert response.status_code == 302
    assert '/' == response.url


@pytest.mark.django_db
def test_save_user_info_after_sign_up_post_request(client):
    client.post('/signup/',
                data={'nickname': 'test nickname',
                      'phone1': '010',
                      'phone2': '1111',
                      'phone3': '2222',
                      'gender': 'M',
                      'email': 'test@naver.com',
                      'password': '12341234'})

    User.objects.get(email='test@naver.com')


@pytest.mark.django_db
def test_redirect_to_homepage_after_sign_up_post_request(client):
    response = client.post('/signup/',
                           data={'nickname': 'test nickname',
                                 'phone1': '010',
                                 'phone2': '1111',
                                 'phone3': '2222',
                                 'gender': 'M',
                                 'email': 'test@naver.com',
                                 'password': '12341234'})

    assert response.status_code == 302
    assert '/' == response.url

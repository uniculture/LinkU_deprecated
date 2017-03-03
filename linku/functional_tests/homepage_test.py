# -*- coding: utf-8 -*-

import sys
import os

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from urllib.parse import urljoin

import pytest

ROOT_URL_DEVELOP = "http://localhost:8000"


@pytest.fixture(scope="module")
def browser():
    if sys.platform == 'darwin':
        project_root = os.path.dirname(os.path.dirname(
            os.path.realpath(__file__)))
        repo_root = os.path.dirname(project_root)
        sys.path.append(os.path.join(repo_root, 'dev'))
        import download_chromedriver
        download_chromedriver.download()
        chrome_path = download_chromedriver.get_chromedriver_path()
        if chrome_path is False:
            raise SystemExit
        driver = webdriver.Chrome(chrome_path)
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_first_page_cards_title(browser):
    # 평소 짱구는 요즘 새로운 사람을 만나고 싶어서 우리 서비스에 접속했다.
    # 서비스에 접속하니
    browser.get(ROOT_URL_DEVELOP)

    # 첫 화면에는 모임에 대한 정보가 보이는 카드들이 보였다.

    # 그 카드 중 하나를 자세히 살펴보니 맨 상단에는 규카츠 먹을래? 제목이 보여졌고,
    assert '규카츠 먹을래?' in browser.page_source

    # 그 아래에는 장선혁(개설자 이름)
    assert '장선혁' in browser.page_source

    # 강남(장소)
    assert '강남' in browser.page_source

    # 02/22 21:52 (시작 시간)
    assert '02/22 21:52' in browser.page_source

    # 규카츠가 맛있게 보이는 사진
    # 고려대학교 10km 이내(가까운 대학교와의 거리)
    assert '고려대학교 10km 이내' in browser.page_source

    # 5,000원~10,000원(가격대)
    assert '5,000원~10,000원' in browser.page_source
    # 들이 보인다.

    # 그 바로 하단에는 선이 그어져 있어서 왠지 서로 구분이 되는 느낌이다
    browser.find_element_by_tag_name('hr')

    # 맨 상단에는 호타루에서 우동 먹을래? 제목이 보여졌고,
    assert '호타루에서 우동 먹을래?' in browser.page_source
    # 그 아래에는 최지훈(개설자 이름)
    assert '최지훈' in browser.page_source
    # 이대(장소)
    assert '이대' in browser.page_source
    # 02/22 22:22 (시작 시간)
    assert '02/22 22:22' in browser.page_source
    # 우동이 맛깔스럽게 보이는 사진
    # 이화여자대학교 10km 이내(가까운 대학교와의 거리)
    assert '이화여자대학교 10km 이내' in browser.page_source
    # 5,000원~10,000원(가격대)
    assert '5,000원~10,000원' in browser.page_source
    # 들이 보인다.

    # 짱구는 두 모임 중에 지훈이의 '호타루 우동 모임'에 참가하고 싶어졌다.
    # 그래서 모임 아래에 신청하기 버튼을 확인한 후,
    btn_list = browser.find_elements_by_tag_name('button')
    assert btn_list[2].text == "신청하기"

    # 신청 버튼을 눌렀더니
    btn_list[2].click()

    # 해당 모임을 신청하는 페이지로 이동하였고
    assert urljoin(ROOT_URL_DEVELOP,
                   "/meetings/2/apply/") == browser.current_url

    # 상단에 "호타루에서 우동 먹을래?" 라는 모임의 제목이 보였다.
    assert "호타루에서 우동 먹을래?" in browser.page_source

    # 이름, 성별, 연락처를 입력하라는 메세지와 입력박스가 표시된다.
    assert "이름 : " in browser.page_source
    assert "연락처 : " in browser.page_source
    assert "성별 : " in browser.page_source

    input_boxs = browser.find_elements_by_tag_name('input')

    # 그래서 짱구는 이름 칸에 '김짱구'라고 입력 했고
    input_boxs[0].send_keys('김짱구')

    # 연락처는 '010-1234-5678' 로 입력하고
    input_boxs[1].send_keys('010-1234-5678')

    # 성별은 '남성'으로 체크하고
    input_boxs[2].click()

    # 신청 버튼을 누르자
    apply_button = browser.find_element_by_tag_name('button')
    apply_button.click()

    # '신청이 완료되었습니다.' 라는 메세지가 표시됐다.
    assert "신청이완료되었습니다." in Alert(browser).text

    # 확인 버튼을 눌렀더니
    Alert(browser).accept()

    # 메인 홈페이지로 이동을 하였다
    assert urljoin(ROOT_URL_DEVELOP, '/') == browser.current_url


def test_specific_page_contents(browser):
    # 로그인을 한 짱구는 첫 페이지로 돌아간다.
    browser.get(ROOT_URL_DEVELOP)

    # "호타루에서 우동 먹을래?"를 보고 세부내용을 보기로 마음 먹는다.
    assert "호타루에서 우동 먹을래?" in browser.page_source

    # 짱구는 "호타루에서 우동 먹을래?"안에 있는 "상세보기"를 확인하고
    btn_list_in_first_page = browser.find_elements_by_tag_name('button')
    assert btn_list_in_first_page[3].text == "상세보기"

    # 짱구는 "상세보기"를 누른다
    btn_list_in_first_page[3].click()

    # "상세보기"를 누르니 상세페이지 주소로 이동하였다.
    assert urljoin(ROOT_URL_DEVELOP,
                   "/meetings/2/") == browser.current_url

    # 상세모임에 들어간 짱구는 크게 가운데에
    # 음식 사진
    # "월/일 장소 시간"의 형태로 날짜 장소 및 시간을 확인 할 수 있었으며
    assert '02/22 이대 22:22' in browser.page_source

    # 모임 제목을 확인할 수 있었고
    assert '호타루에서 우동 먹을래?' in browser.page_source

    # 모임장의 사진과 모임에 대한 소개가 있는것을 확인한다.
    # 모임장은 "최지훈"이다
    assert '모임장' in browser.page_source
    assert '최지훈' in browser.page_source

    # 그 아래는 참여자를 나타내는 박스와 참여자의 프로필 사진들이 있다.
    assert '참여자' in browser.page_source

    # 그 아래는 위치와 위치의 지도가 나타나있다
    assert '위치' in browser.page_source

    # 그 아래는 댓글 창이 있는 것을 확인 했다.
    assert '댓글' in browser.page_source

    # 우측에는 모임에 대한 정보 요약이 있으며

    # 위치, 시간, 모집인원, 성비, 예상비용이 나타나있다.
    assert '위치' in browser.page_source
    # 장소는 "이대"이며
    assert '이대' in browser.page_source

    assert '시간' in browser.page_source
    # 시간은 "22:22"였고
    assert '22:22' in browser.page_source

    # 모집인원 3명중에 참여된 인원은 2명이었다.
    assert '모집인원' in browser.page_source
    assert '2/3' in browser.page_source

    assert '성비' in browser.page_source

    assert '예상비용' in browser.page_source
    # 가격은 '5,000원~10,000원'이다.
    assert '5,000원~10,000원' in browser.page_source

    # 예상비용 아래 "오케이 콜!"과 "♡찜하기"라는 버튼이 있었다
    sidebar = browser.find_element_by_id('sidebar')
    btn_list_in_sidebar = sidebar.find_elements_by_tag_name('button')

    assert btn_list_in_sidebar[0].text == '오케이 콜!'
    assert btn_list_in_sidebar[1].text == '♡찜하기'

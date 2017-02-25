# -*- coding: utf-8 -*-

import sys
import os

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

import pytest


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
    browser.get("http://localhost:8000")

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
    assert btn_list[1].text == "신청하기"

    # 신청 버튼을 눌렀더니
    btn_list[1].click()

    # 해당 모임을 신청하는 페이지로 이동하였고
    assert "/meetings/2/apply" in browser.current_url

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
    Alert(browser).accept()

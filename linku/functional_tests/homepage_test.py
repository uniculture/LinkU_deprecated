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
    assert btn_list[3].text == "신청하기"

    # 신청 버튼을 눌렀더니
    btn_list[3].click()

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
    input_boxs[1].send_keys('01012345678')

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


def test_applying_page_when_user_wrote_wrong_input(browser):
    # 짱구는 이번에는 첫 번째 모임인 선혁이의 "규카츠 먹을래?" 모임에 참가하기 위해 사이트에 접속한 후 신청하기 버튼을 눌렀다.
    browser.get(ROOT_URL_DEVELOP)
    btn_list = browser.find_elements_by_tag_name('button')
    btn_list[1].click()

    # 짱구는 아무것도 입력하지 않은 상태로 확인 버튼을 눌러본다.
    apply_button = browser.find_element_by_tag_name('button')
    apply_button.click()

    # '잘못된입력입니다." 라는 메세지의 팝업창이 뜬다.
    assert "잘못된입력입니다." in Alert(browser).text

    # 확인 버튼을 눌러서 팝업창을 닫고
    Alert(browser).accept()

    # 이번에는 이름과 성별을 '김짱구', '남'으로 입력하고,
    input_boxs = browser.find_elements_by_tag_name('input')
    input_boxs[0].send_keys('김짱구')
    input_boxs[2].click()

    # 연락처는 연락처 형식에 맞지 않는 '15152'을 입력해보기로 한다.
    input_boxs[1].send_keys('15152')

    # 다시 신청 버튼을 누르자
    apply_button.click()

    # '잘못된입력입니다.' 라는 팝업창이 다시 떴다.
    assert "잘못된입력입니다." in Alert(browser).text

    # 확인 버튼을 눌러서 팝업창을 닫고
    Alert(browser).accept()

    # 연락처를 다시 '01011111111'으로 올바르게 입력한 후
    input_boxs[1].clear()
    input_boxs[1].send_keys('01011111111')

    # 다시 신청 버튼을 누르자
    apply_button.click()

    # '신청이완료되었습니다.' 라는 메세지가 표시되고 메인 홈페이지로 이동하였다.
    assert "신청이완료되었습니다." in Alert(browser).text
    Alert(browser).accept()


def test_specific_page_contents(browser):
    # 로그인을 한 짱구는 첫 페이지로 돌아간다.
    browser.get(ROOT_URL_DEVELOP)

    # "호타루에서 우동 먹을래?"를 보고 세부내용을 보기로 마음 먹는다.
    assert "호타루에서 우동 먹을래?" in browser.page_source

    # 짱구는 "호타루에서 우동 먹을래?"안에 있는 "상세보기"를 확인하고
    btn_list_in_first_page = browser.find_elements_by_tag_name('button')
    assert btn_list_in_first_page[4].text == "상세보기"

    # 짱구는 "상세보기"를 누른다
    btn_list_in_first_page[4].click()

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


def test_signup_page(browser):
    # 평소 짱구는 요즘 새로운 사람을 만나고 싶어서 우리 서비스에 접속했다.
    # 서비스에 접속하니
    browser.get(ROOT_URL_DEVELOP)

    # 회원가입 버튼이 최상단에서 보였고,
    sign_up_button = browser.find_element_by_name('signup')

    # 자세히 읽어보니 그 버튼 안에는 회원가입 이라고 적혀있었다.
    assert "회원가입" == sign_up_button.text

    # 짱구는 일단 뭐든 회원가입이 먼저라고 생각하는 사람이라, 주저하지 않고 회원가입을 클릭했다
    sign_up_button.click()

    # 회원가입을 클릭하니 회원가입 페이지로 이동했고,
    assert urljoin(ROOT_URL_DEVELOP,
                   "/signup/") == browser.current_url

    # 페이지의 타이틀은 '회원가입'이라고 적혀있었으며
    assert '회원가입' == browser.title

    # 페이지 최상단에는 굵은 글씨로
    h1_tag = browser.find_element_by_tag_name('h1')

    # '회원가입'이라고 적혀있었고
    assert '회원가입' == h1_tag.text

    # 바로 하단에는 조금더 작은 글씨로
    h2_tag = browser.find_element_by_tag_name('h2')

    # '어서와 링쿠는 처음이지?'라고 적혀있었다
    assert '어서와 링쿠는 처음이지?' == h2_tag.text

    # 그 바로 옆에는 이메일을 입력할 입력 박스가 있었고
    email_box = browser.find_element_by_xpath("//input[@name='email']")

    # 짱구는 그 안에다 자신의 이메일인 'jjangu@gmail.com'라고 입력하였다.
    email_box.send_keys('jjangu@gmail.com')

    # 바로 왼쪽에는 '이메일:' 이라고 적혀있었다.
    email_label = browser.find_element_by_xpath("//label[@for='email']")
    assert '이메일:' == email_label.text

    # 또 바로 옆에는 중복확인 버튼이 있었다.
    dup_chk_btn = browser.find_element_by_xpath("//button[@name='email_dup_chk']")
    assert '중복확인' == dup_chk_btn.text

    # 그 아래에는 '비밀번호:'라 적혀있었고
    pwd_label = browser.find_element_by_xpath("//label[@for='password']")
    assert '비밀번호:' == pwd_label.text

    # 그 바로 옆에는 비밀번호를 입력할 입력 박스가 있었다.
    pwd_box = browser.find_element_by_xpath("//input[@name='password']")

    # 그래서 짱구는 자신이 좋아하는 비밀번호 '1q2w3e4r!'를 입력했다
    pwd_box.send_keys('1q2w3e4r!')

    # 그 아래에는 비밀번호 확인이라 적혀있었고
    pwd_chk_label = browser.find_element_by_xpath("//label[@for='password_check']")
    assert '비밀번호 확인:' == pwd_chk_label.text

    # 그 바로 옆에는 비밀번호 확인을 입력할 입력박스가 있었고,
    pwd_chk_box = browser.find_element_by_xpath("//input[@name='password_check']")

    # 그래서 짱구는 같은 비밀번호 '1q2w3e4r!'를 입력하였다.
    pwd_chk_box.send_keys('1q2w3e4r!')

    # 그 아래에는 성별이 적혀있었고
    gender_label = browser.find_element_by_xpath("//label[@for='gender']")
    assert '성별:' == gender_label.text

    # 그 바로 옆에는 라디오 버튼과,
    male_radio = browser.find_element_by_id('male')

    # 라디오 버튼에 딸려있는 라벨인 '남자'
    male_label = browser.find_element_by_xpath("//label[@for='male']")
    assert '남자' == male_label.text

    # 또 바로 옆에는 라디오 버튼이 있었고
    female_radio = browser.find_element_by_id('female')

    # '여자'라는 라벨이 딸려있었다.
    female_label = browser.find_element_by_xpath("//label[@for='female']")
    assert '여자' == female_label.text

    # 철수는 남자라서 남자에 체크했다
    male_radio.click()

    # 그 아래에는 닉네임 입력이라 적혀있었고
    nickname_label = browser.find_element_by_xpath("//label[@for='nickname']")
    assert '닉네임 입력:' == nickname_label.text

    # 그 바로 옆에는 닉네임을 입력할 입력 박스가 있었다.
    nickname_input = browser.find_element_by_name('nickname')

    # 짱구는 '짱구는 못말려'를 입력했다.
    nickname_input.send_keys('짱구는 못말려')

    # 밑에는 프로필 사진이 적혀있었고
    profile_label = browser.find_element_by_xpath("//label[@for='profile']")
    assert '프로필 사진' == profile_label.text

    # 그 바로 옆에는 프로필 사진을 첨부할 수 있도록 '첨부'라 적혀있는 버튼이 있었다
    profile_atchmnt_btn = browser.find_element_by_xpath("//button[@name='profile']")
    assert '첨부' == profile_atchmnt_btn.text

    # 그 아래에는 휴대폰 번호라 적혀있었고
    phone_label = browser.find_element_by_xpath("//label[@for='phone1']")
    assert "휴대폰 번호:" == phone_label.text

    # 그 바로 옆에는 휴대폰을 입력할 3개의 입력 박스가 나란히 있었다.
    phone_bx_1 = browser.find_element_by_xpath("//input[@name='phone1']")
    phone_bx_2 = browser.find_element_by_xpath("//input[@name='phone2']")
    phone_bx_3 = browser.find_element_by_xpath("//input[@name='phone3']")

    # 첫번째 입력박스에 '1244'를 쳤더니 '124'까지만 입력이 되었다
    phone_bx_1.send_keys('1244')
    assert '124' == phone_bx_1.get_attribute('value')

    # 그래서 짱구는 각 칸에 010, 1234, 5678을 입력했다.
    phone_bx_1.send_keys('010')
    phone_bx_2.send_keys('1234')
    phone_bx_3.send_keys('5678')

    # 그리고 바로 밑에는 안심번호를 사용할 수 있도록 체크박스 버튼 하나와
    comfor_num_chkbox = browser.find_element_by_xpath("//input[@name='comfortable_num']")

    # '안심번호 사용하기'라는 라벨이 붙어있었다.
    comfor_num_label = browser.find_element_by_xpath("//label[@for='comfortable_num']")
    assert '안심번호 사용하기' == comfor_num_label.text

    # 짱구는 안심번호를 사용하고 싶어서 안심번호 사용하기를 체크했다.
    comfor_num_chkbox.click()

    # 그리고 대학생 신분을 인증하기 위해, '신분 인증'이라는 라벨과 함께
    verification_label = browser.find_element_by_xpath("//label[@for='verification']")
    assert '신분 인증:' == verification_label.text

    # 바로 오른쪽에 입력박스가 있었으며,
    verification_box = browser.find_element_by_xpath("//input[@name='verification']")

    # 메일 인증이라는 버튼이 있었다
    verification_btn = browser.find_element_by_xpath("//button[@name='verification']")
    assert '메일 인증' == verification_btn.text

    # 단국대생인 짱구는 메일 인증을 위해 입력박스에 자신의 메일인 'jjangu@dankook.ac.kr'를 입력했다.
    verification_box.send_keys('jjangu@dankook.ac.kr')

    # 그리고 가입을 취소하기 위한 취소버튼이 바로 아래 쪽에 있었고
    cancel_btn = browser.find_element_by_xpath("//button[@name='cancel']")

    # 내용은 '취소'라고 적혀있었다
    assert '취소' == cancel_btn.text

    # 그리고 바로 옆에는 버튼이 있었는데
    confirm_btn = browser.find_element_by_xpath("//button[@name='confirm']")

    # 거기엔 '가입완료'라고 적혀있었다.
    assert '가입완료' == confirm_btn.text

    # 짱구는 모든 정보를 입력해서 가입완료 버튼을 눌렀다
    confirm_btn.click()

    # 가입이 완료되었습니다. 라는 팝업이 생겨서,
    assert "가입이 완료되었습니다." == Alert(browser).text

    # 확인 버튼을 눌렀더니
    Alert(browser).accept()

    # 메인 홈페이지로 이동을 하였다
    assert urljoin(ROOT_URL_DEVELOP, '/') == browser.current_url

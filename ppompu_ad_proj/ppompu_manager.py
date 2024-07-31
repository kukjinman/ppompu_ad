from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium_util import init_browser
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.ppomppu.co.kr/zboard/zboard.php?id=worker"

def run_ppompu_browser():
    print("run_ppompu_browser is called")
    global browser
    browser = init_browser(url)

def write_newpost():
    print("write_newpost is called")
    newpost_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#bottom-table > div.info_bg > a.write_btn"))
    )

    newpost_btn.click()

    author_pw = browser.find_element(By.CSS_SELECTOR,"#ps_in")
    author_pw.send_keys("1234")

    title_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#divSubject > td > input"))
    )
    title_input.send_keys("파이썬 블로그 자동화 프로그램 유튜브!!")

    body_iframe = browser.find_element(By.CSS_SELECTOR,"body > div.wrapper > div.contents > div.container > div > form > table > tbody > tr > td > table:nth-child(2) > tbody > tr:nth-child(4) > td > div.cheditor-container > div.cheditor-editarea-wrapper > iframe:nth-child(1)")
    browser.switch_to.frame(body_iframe)

    global body
    body = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "body"))
    )
    message = (
        "-- 본 포스트는 자동화 프로그램으로 작성된 글입니다. --\n\n"
        "안녕하세요. SW비전공자 국진맨입니다.\n\n"
        "SW직군이 아닌데 회사에 SW직군으로 들어가게 되었습니다. \n"
        "SW교육에서는 간단한 print도 출력하지 못했습니다.\n\n"
        "사내 sw교육에서 200명중에 뒤에서 3등 하던 제가 \n"
        "현재는 차량 SW의 system, diag, broadcast등 다수의 코딩을 구현하였고,\n"
        "그 외로 웹페이지, 안드로이드 앱 개발, 파이썬 자동화 프로그램등을 만들었습니다.\n\n"
        "대학에서 SW전공으로 졸업 안하셨다고요? 괜찮습니다. \n\n"
        "조금씩 꾸준히만 하시면 그 시간이 누적되어 \n"
        "다른 사람들이 노는 시간에 저희는 개발의 역량이 조금씩 쌓여 \n"
        "전문가 소리를 들으실 겁니다.\n\n"
        "열정이 있으신 분들께 조금이나마 도움이 되고자 만든 체널입니다.\n\n"
        "실제 학원에서 2개월 100만원의 비용을 내야 배울 수 있는 \n"
        "파이썬 자동화 프로그램 교육을 제공합니다.\n\n\n\n"
        "강의료는 구독입니다.\n\n"
        "유튜브 URL: https://youtube.com/@kukjinman?si=dG80Yb7WD94RXewv"
    )

    body.send_keys(message)


def body_stytling():
    print("write_newpost is called")

    ActionChains(browser).click(body)
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    browser.switch_to.default_content()

    font_size_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "body > div.wrapper > div.contents > div.container > div > form > table > tbody > tr > td > table:nth-child(2) > tbody > tr:nth-child(4) > td > div.cheditor-container > div.cheditor-tb-wrapper > div.cheditor-tb-bg40 > div"))
    )
    font_size_element.click()

    font_size_20px = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="20px"]'))
    )
    font_size_20px.click()

    center_align_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrapper > div.contents > div.container > div > form > table > tbody > tr > td > table:nth-child(2) > tbody > tr:nth-child(4) > td > div.cheditor-container > div.cheditor-tb-wrapper > div:nth-child(20)"))
    )

    center_align_btn.click()

    publish_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ok_button"))
    )

    publish_btn.click()


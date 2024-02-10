from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import logging



def setup():
    global browser
    browser = webdriver.Chrome()
    browser.get('https://sbis.ru/')
    browser.maximize_window()


sleep_time = 0.5
us_location = 'Республика Башкортостан'
region = 'Камчатский край'

def first_url():
    return browser.current_url

def contacts():
    browser.find_element(By.XPATH, '//li[@class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]').click()

def f_page():
    first_page = browser.find_element(By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]').text
    return first_page

def f_reg_num():
    f_num = ((browser.find_element(By.XPATH, f'//span[@title="{region}"]')).text).split(' ')[0]
    return f_num

def new_region():
    set_region = browser.find_element(By.XPATH, f'//span[@title="{region}"]')
    global b 
    b = f_reg_num()
    set_region.click()
    sleep(sleep_time)

def test_location():
    contacts()
    global a, c
    a = f_page()
    c = first_url
    location = browser.find_element(By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    assert location.text == us_location, 'Регион не изменился'
    location.click()
    sleep(sleep_time) 
     
def test_new_url():
    new_region()
    assert browser.current_url != c, 'URL не изменился'

def test_page():
    assert a != browser.find_element(By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]').text, 'Список партнеров не изменился'

def test_reg():
    assert b == ((browser.current_url.split('/'))[-1].split('-'))[0], 'В URL указан неправильный регион'

def test_title():
    title = browser.title
    reg_arr = region.split(' ')
    title_arr = title.split(' ')
    k = 0
    for i in range(len(reg_arr)):
        if reg_arr[i] in title_arr:
            continue
        else:
            k += 1
    assert k == 0, 'В title указан неправильный регион'

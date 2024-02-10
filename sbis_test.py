from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



sleep_time = 2

def setup():
        global browser
        browser = webdriver.Chrome()
        browser.maximize_window()

def sbis():
        browser.get('https://sbis.ru')
        click_contacts = browser.find_element(By.XPATH, '//li[@class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]')
        click_contacts.click()

        sleep(sleep_time)

        click_tensor = browser.find_element(By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]')
        click_tensor.click()

        sleep(sleep_time)

        browser.switch_to.window(browser.window_handles[1])

def test_tensor():
        sbis()
        search_people = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')

        assert search_people.text == 'Сила в людях'

        click_about = browser.find_element(By.XPATH, ('//div[@class="tensor_ru-Index__block4-bg"]//a[@class="tensor_ru-link tensor_ru-Index__link"]'))
        browser.execute_script("arguments[0].scrollIntoView();", click_about)

        sleep(sleep_time)

        click_about.click()

def test_url():
        assert browser.current_url == 'https://tensor.ru/about'

        sleep(sleep_time)

def test_img():
        images = browser.find_element(By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]/div[@class="s-Grid-container"]').find_elements(By.TAG_NAME, 'img')

        val = None
        count = 1

        for image in images:
            if val == None:
                val = image.size
            else:
                if val == image.size:
                    count += 1
                    continue
                else:
                    print('---')
                    break

        assert count == 4
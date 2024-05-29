import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.feature('Регистрация и Вход')
@allure.story('Тест регистрации и входа на сайт')
def test_registration_and_login():
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.add_argument('--start-maximized')
    browser = webdriver.Firefox(options=firefox_option)

    with allure.step('Открываем сайт'):
        browser.get('http://localhost:3000/')
        time.sleep(1.5)

    with allure.step('Открываем меню'):
        element = browser.find_element(By.XPATH, "//div[@class='home-page']//img[@alt='Menu Icon']")
        element.click()
        time.sleep(1.5)

    with allure.step('Переходим на страницу регистрации'):
        element = browser.find_element(By.XPATH, "//nav[@class='nav open']//a[@class='nav-link'][contains(text(),'Регистрация')]")
        element.click()
        time.sleep(0.5)

    with allure.step('Заполняем поле Email'):
        element = browser.find_element(By.XPATH, "//div[@class='registration-page']//div[1]//input[1]")
        element.send_keys("sevateti2@yandex.com")
        time.sleep(0.5)

    with allure.step('Заполняем поле имени'):
        element = browser.find_element(By.XPATH, "(//input[@type='text'])[2]")
        element.send_keys("Vsevolod")
        time.sleep(0.5)

    with allure.step('Заполняем поле пароля'):
        element = browser.find_element(By.XPATH, "(//input[@type='password'])[1]")
        element.send_keys("Ctdf20051906")
        time.sleep(0.5)

    with allure.step('Подтверждаем пароль'):
        element = browser.find_element(By.XPATH, "(//input[@type='password'])[2]")
        element.send_keys("Ctdf20051906")
        time.sleep(0.5)

    with allure.step('Заполняем поле дополнительной информации'):
        element = browser.find_element(By.XPATH, "(//input[@type='text'])[3]")
        element.send_keys("12")
        time.sleep(0.5)

    with allure.step('Нажимаем кнопку "Зарегистрироваться"'):
        element = browser.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
        element.click()
        time.sleep(1.5)

    with allure.step('Открываем меню2'):
        element = browser.find_element(By.XPATH, "(//img[@alt='Menu Icon'])[1]")
        element.click()
        time.sleep(1.5)

    with allure.step('Переходим на страницу входа'):
        element = browser.find_element(By.XPATH, "//a[contains(text(),'Вход')]")
        element.click()
        time.sleep(1)

    with allure.step('Вводим имя пользователя'):
        element = browser.find_element(By.XPATH, "//input[@type='text']")
        element.send_keys("Vsevolod")
        time.sleep(1.5)

    with allure.step('Вводим пароль'):
        element = browser.find_element(By.XPATH, "(//input[@type='password'])[1]")
        element.send_keys("Ctdf20051906")
        time.sleep(0.5)

    with allure.step('Нажимаем кнопку "Скачать"'):
        element = browser.find_element(By.XPATH, "(//button[contains(text(),'Войти')])[1]")
        element.click()

    with allure.step('Нажимаем кнопку "Скачать"'):
        element = browser.find_element(By.XPATH, "(//button[contains(text(),'Скачать')])[1]")
        element.click()

    input("Нажмите Enter для завершения работы")

    browser.quit()

if __name__ == "__main__":
    test_registration_and_login()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(s):
    return str(math.log(abs(12*math.sin(int(s)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока цена не станет меньше или равна $100
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_to_buy = browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text  # поиск и запись значения Х
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")  # поиск поля для записи ответа
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve").click()  # Отправляем заполненную форму
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

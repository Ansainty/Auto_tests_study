from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    treasure = browser.find_element(By.ID, "treasure")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Отправляем заполненную форму
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)    # вывод результата
    alert.accept()

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

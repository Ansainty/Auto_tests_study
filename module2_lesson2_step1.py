from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    
    total = (int(num1)+int(num2))
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)    # вывод результата
    alert.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

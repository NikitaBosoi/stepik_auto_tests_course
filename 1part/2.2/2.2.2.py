from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    parse1 = browser.find_element_by_css_selector("#num1")
    num1 = parse1.text
    parse2 = browser.find_element_by_css_selector("#num2")
    num2 = parse2.text
    sum = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
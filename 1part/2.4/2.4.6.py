from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    
    button = browser.find_element_by_id("button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
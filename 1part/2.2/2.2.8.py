from selenium import webdriver
import time
import math
import os

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    elements = browser.find_elements_by_css_selector("[type='text']")
    for element in elements:
        element.send_keys("Ответ")
        
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    upload = browser.find_element_by_css_selector("#file")
    upload.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
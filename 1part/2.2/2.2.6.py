from selenium import webdriver
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", option2)
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
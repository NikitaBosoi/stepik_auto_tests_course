from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)

    browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys('f_n')
    browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys('l_n')
    browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys('p@s')
    browser.find_element_by_css_selector("[placeholder='Input your phone:']").send_keys('103')
    browser.find_element_by_css_selector("[placeholder='Input your address:']").send_keys('home')

    browser.find_element_by_xpath("//button[text()='Submit']").click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name('h1').text
    assert 'Congratulations' in welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

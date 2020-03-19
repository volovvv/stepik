import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(y)



    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)



finally:
    time.sleep(5)
    browser.quit()

import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(1)



finally:
    time.sleep(5)
    browser.quit()

import math
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    print(x)
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    print(y)
    s = str(int(x)+int(y))
    print(s)
    s="[value='" + s +"']"
    print(s)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(s).click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)



finally:
    time.sleep(5)
    browser.quit()

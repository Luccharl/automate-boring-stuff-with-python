import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

while True:
    html = browser.find_element_by_tag_name('html')
    html.send_keys(Keys.ARROW_UP)
    html.send_keys(Keys.ARROW_RIGHT)
    html.send_keys(Keys.ARROW_DOWN)
    html.send_keys(Keys.ARROW_LEFT)
        
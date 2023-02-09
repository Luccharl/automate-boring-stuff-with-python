from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print(f'Found <{elem.tag_name}> element with that class name')
except:
    print('Unable to find element with that class name')
import time

from selenium import webdriver

def get_results(search_term):
    browser = webdriver.Chrome('Resources/chromedriver.exe')
    browser.get("http://www.google.com/")
    browser.maximize_window()
    browser.delete_all_cookies()
    search_box = browser.find_element_by_name('q')
    search_box.send_keys(search_term)
    search_box.submit()
    time.sleep(5)



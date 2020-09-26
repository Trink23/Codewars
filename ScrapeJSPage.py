from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrapeJSpage(url):
    driver = webdriver.Chrome('Resources/chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    result = soup.find(id='profile')
    print(result.prettify())

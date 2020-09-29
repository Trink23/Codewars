from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrapeJSpage(url):
    driver = webdriver.Chrome('Resources/chromedriver.exe')
    driver.get(url)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    result = soup.find(id='profile')
    job_elems = soup.find_all(['th', 'td'])
    print(result.prettify())
    for job_elem in job_elems:
        print(job_elem, end='\n' * 2)

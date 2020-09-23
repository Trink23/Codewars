import requests
from bs4 import BeautifulSoup

def scrapHTML(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(id = 'profile')
    print(result.prettify())

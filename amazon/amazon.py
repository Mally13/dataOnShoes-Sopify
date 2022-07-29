from bs4 import BeautifulSoup
from requests_html import HTMLSession

from requests_html import HTMLSession
s = HTMLSession()
url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
getdata(url)

def getnextpage(soup):
    page = soup.find('span', {'class': 's-pagination-item'})
    if not page.find('span', {'class': 's-pagination-disabled'}):
        url = 'https://www.amazon.com' + str(page.find('span',{'class':'s-pagination-disabled'}).find('a')['href'])
while True:   
    soup = getdata(url)
    print(getnextpage(soup))
    if not url:
        break
    

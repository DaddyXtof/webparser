import requests
import bs4

target = "http://onecloudstreet.com"
site = requests.get(target)
print(site.content)
soup = bs4.BeautifulSoup(site.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

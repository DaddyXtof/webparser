import requests
import bs4

target = "http://onecloudstreet.com"
site = requests.get(target)
print(site.content)
import requests
import bs4
import argparse

def retrieveURL(url):
    print("#### Retrieving: "+ url)
    site = requests.get(target)
    # print(site.content)
    soup = bs4.BeautifulSoup(site.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

my_parser = argparse.ArgumentParser(description='Crawl URL and list all <a> links found')
my_parser.add_argument('url',
                       metavar='url',
                       type=str,
                       help='the URL to crawl - for example: http://onecloudstreet.com')
args = my_parser.parse_args()
target = args.url
retrieveURL(target)


import requests
import bs4
import argparse
import tldextract

alreadyvisited = [] # list of urls that have already been crawled

def retrieveURL(turl):
    print("#### Retrieving: "+ turl)
    alreadyvisited.append(turl) # keeping track of urls already visited
    currentpagelinks = [] # list of links on the page being parsed
    site = requests.get(turl)
    soup = bs4.BeautifulSoup(site.content, 'html.parser')
    for link in soup.find_all('a'):
        linkstring = link.get('href')
        if linkstring is not None:
            if linkstring[0:4].lower() == 'http': # ignoring anchors etc...
                print('\t' + linkstring)
                currentpagelinks.append(linkstring)
        
    if currentpagelinks: # we have links to follow
        for linkstring in currentpagelinks:
            if not linkstring in alreadyvisited and domain in linkstring:
                retrieveURL(linkstring)


my_parser = argparse.ArgumentParser(description='Crawl URL and list all <a> links found')
my_parser.add_argument('url',
                       metavar='url',
                       type=str,
                       help='the URL to crawl - for example: http://onecloudstreet.com')
args = my_parser.parse_args()
target = args.url
ext = tldextract.extract(target)
domain = ext.registered_domain
print ("#### Domain: "+ domain)
retrieveURL(target)


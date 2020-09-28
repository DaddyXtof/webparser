"# webparser" 
* Crawler exercise progress:
From memory I believe it is possible to crawl/download a site using
wget. It may be possible to generate the map file from a wget ouptut.
Indeed - after doing some browsing and checking this page
(https://www.labnol.org/software/wget-command-examples/28750/) it
appears that the following wget command will retrieve the site: wget
‐‐output-file=logfile.txt ‐‐recursive -nd ‐‐spider
http://wiprodigital.com 
It seems to work but the log file generated contains more than what we
are trying to generate and would need parsing. There are probably ways
to do this parsing with regular expression and a corresponding shell
utility but this is not something I am immediately familiar with.
When working with Python I do recall mentions of Beautiful Soup as a
web scraper library that may be of use here.


What we want to create is a CLI python application which can take the
following arguments:

> webparser.py http://someurl.com

** required: URL to scrape
** Option: only show links for the current domain
** Option: only show links for external sites

We will need to retrieve the HTML content and parse it. So we need the
library requests (to issue the HTTP request) and beautifulsoup to
parse the content and navigate it.  We want this to be a CLI tool so
we can use the argparse library to manage arguments elegantly.  I also
added tldextract library in order to retrieve the top level domain
of the URL.

----

usage: webparser.py [-h] [-i] [-e] url

Crawl URL and list all <a> links found

positional arguments:
  url             the URL to crawl - for example: http://onecloudstreet.com

optional arguments:
  -h, --help      show this help message and exit
  -i, --internal  only list internal links (to the TLD)
  -e, --external  only list external links (to the TLD)

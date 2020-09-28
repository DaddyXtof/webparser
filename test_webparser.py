import webparser

target = "http://onecloudstreet.com"
ext = webparser.tldextract.extract(target)
domain = ext.registered_domain
webparser.retrieveURL(target)

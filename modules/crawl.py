from bs4 import BeautifulSoup
import requests as r
import lxml as lxml
import datetime

# Somewhat heavily reliant on https://practicaldatascience.co.uk/data-science/how-to-parse-xml-sitemaps-using-python

def request(s):
    t = r.get(s)

    log = open("requestlog.txt", "a")
    log.write(str(s) + "," + str(t.status_code) + "," + str(datetime.datetime.now()) + "\n")
    log.close()

    if t.status_code == 200:
        print(f"successfully requested {s}")
        return t

    else:
        print(f"error requesting {s}: {t.status_code}")
        return False

def getXML(s):
    response = request(s)
    if not response:
        exit()
    if not response.encoding:
        encoding = "utf-8"
    else:
        encoding = response.encoding
    xml = BeautifulSoup(response.content, 'lxml-xml', from_encoding=encoding)
    return xml

# add capability for RSS and ATOM feeds

def sitemapType(x):
    sitemapindex = x.find_all("sitemapindex")
    urlset = x.find_all("urlset")
    if sitemapindex: 
        return "sitemapindex"
    elif urlset:
        return "urlset"
    else:
        print("Unrecognized sort of sitemap.")
        return False

# ok so none of my sitemaps have child sitemaps, but just in case. Integrate it if you want more functionality.

def getChildSitemaps(x):
    sitemaps = x.find_all("sitemap")
    o = []
    for sitemap in sitemaps:
        o.append(sitemap.findNext("loc").text)
    return o

# returns the overall list of urls

def getURLs(x):
    urls = x.find_all("url")
    o = []
    for url in urls:
        o.append(url.findNext("loc").text)
    return o

def getHTML(s):
    response = request(s)
    if response:
        if not response.encoding:
            encoding = "utf-8"
        else:
            encoding = response.encoding
        html = BeautifulSoup(response.content, 'lxml-html', from_encoding=encoding)
        return html

def HTMLcorpus(s):
    x = getXML(s)
    list = getURLs(x)
    html = []
    for l in list:
        h = getHTML(l)
        html.append(h)
    return html

def crawl(s):
    html = HTMLcorpus(s)
    corpus = ""
    for h in html:
        x = 1
    return corpus
from bs4 import BeautifulSoup
import requests as r
import lxml as lxml
import datetime

# Somewhat heavily using the instructions https://practicaldatascience.co.uk/data-science/how-to-parse-xml-sitemaps-using-python

# HTML requests with error handling and logging
errorpages = []
def request(s):
    t = r.get(s)

    # write to a request log to help explain my web analytics
    log = open("requestlog.txt", "a")
    log.write(str(s) + "," + str(t.status_code) + "," + str(datetime.datetime.now()) + "\n")
    log.close()

    # error handling in case there is an error; otherwise we'll end up including error pages in our HTML corpus. 
    if t.status_code == 200:
        print(f"successfully requested {s}")
        return t

    else:
        # save all the errors to a list and tell other functions to ignore this page
        print(f"error requesting {s}: {t.status_code}")
        errordata = {"url": str(s), "statusCode": t.status_code}
        errorpages.append(errordata)
        return False

def getXML(s):
    response = request(s)
    if not response:
        # because we don't have much reason to continue unless a sitemap is available. 
        print("Error requesting XML sitemap. Exiting program.")
        exit() 
    # because sometimes people like me don't always properly format our XML, let's guess... 😬
    if not response.encoding:
        encoding = "utf-8"
    else:
        encoding = response.encoding
    xml = BeautifulSoup(response.content, 'lxml-xml', from_encoding=encoding)
    return xml

# TODO: add capability for RSS and ATOM feeds

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

# none of *my* sitemaps have child sitemaps, but this would add flexibility. Right now this function doesn't actually get called. 
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

# make a BeautifulSoup object from an HTML page
def getHTML(s):
    response = request(s)
    if response:
        if not response.encoding:
            encoding = "utf-8"
        else:
            encoding = response.encoding
        html = BeautifulSoup(response.content, 'lxml-html', from_encoding=encoding)
        return html
    else:
        return False

# makes a list containing every HTML page
def HTMLcorpus(s):
    x = getXML(s)
    list = getURLs(x)
    html = []
    for l in list:
        h = getHTML(l)
        if h:
            html.append(h)
    return html

# extracts text from an HTML page
def extractText(h):
    # we'll take a few guesses at how the author uses semantic HTML
    if h.main:
        content = h.main
    elif h.body:
        content = h.body
    else:
        content = h
    # now we'll delete blockquotes
    if content.blockquote:
        for x in content.find_all("blockquote"):
            x.string = ""
    # extract the remaining text
    text = content.get_text()
    return text

# TODO: filter that there is indeed worthwile text. 
def ofSubstance(t):
    return True 

# extracting the text from the HTML
def text(s):
    html = HTMLcorpus(s)
    corpus = ""
    for h in html:
        text = extractText(h)
        if ofSubstance(text):
            corpus = corpus + text
        else:
            corpus = corpus
    return corpus

def crawl(s):
    return text(s)
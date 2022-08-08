from bs4 import BeautifulSoup
import requests as r
import lxml as lxml
import datetime
import time

# Somewhat heavily using the instructions https://practicaldatascience.co.uk/data-science/how-to-parse-xml-sitemaps-using-python

# HTML requests with error handling and logging
errorpages = []
def request(s, i = 0):
    try:
        t = r.get(s)
        # write to a request log to help explain my web analytics
        log = open("requestlog.txt", "a")
        log.write(str(s) + "," + str(t.status_code) + "," + str(datetime.datetime.now()) + "\n")
        log.close()

        # error handling in case there is an HTTP error; otherwise we'll end up including error pages in our HTML corpus. 
        if t.status_code == 200:
            print(f"successfully requested {s}")
            return t

        else:
            # save all the errors to a list and tell other functions to ignore this page
            print(f"error requesting {s}: {t.status_code}")
            errordata = {"url": str(s), "statusCode": t.status_code}
            errorpages.append(errordata)
            return False
    except Exception as e:
        # if there's some other sort of error, wait a few seconds, and then try again five times.
        print(e)
        if i < 5:
            time.sleep(5)
            i += 1
            request(s, i)
        errordata = {"url": str(s), "statusCode": str(e)}
        errorpages.append(errordata)
        return False

def getXML(s):
    response = request(s)
    if not response:
        # because we don't have much reason to continue unless a sitemap is available. 
        print("Error requesting XML sitemap. Exiting program.")
        exit() 
    # because sometimes people like me don't always properly format our XML, let's guess what encoding... 😬
    if not response.encoding:
        encoding = "utf-8"
    else:
        encoding = response.encoding
    # this will give an exception if a non-XML document is returned; while I could so something like in `getHTML()`, I decided not to because an exception here should end the program. 
    xml = BeautifulSoup(response.content, 'lxml-xml', from_encoding=encoding)
    return xml

# TODO: add capability for RSS/ATOM feeds and sitemaps with child sitemaps

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
    # make sure that it is a valid response and is actually HTML. We'll trust the server, though that might not be the best idea in real life.
    if response and response.headers["Content-type"].find("text/html") >= 0:
        if not response.encoding:
            encoding = "utf-8"
        else:
            encoding = response.encoding
        html = BeautifulSoup(response.content, 'lxml-html', from_encoding=encoding)
        return html
    else:
        return False

# makes a list containing every HTML page
def HTMLcorpus(s, json=False):
    x = getXML(s)
    list = getURLs(x)
    html = []
    for l in list:
        h = getHTML(l)
        if h:
            # because we can't serialize BeautifulSoup objects into JSON
            if json:
                h = str(h)
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

# filter that this is indeed a contentful page
# TODO: do this with natural language processing or something a bit more precise; as is, this only works on a specific design pattern...
def ofSubstance(h):
    if h.title.get_text().find("Tagged") >= 0 or h.title.get_text().find("Tags") >= 0:
        return False
    else:
        return True

# extracting the text from the HTML
def text(s):
    html = HTMLcorpus(s)
    corpus = ""
    for h in html:
        if ofSubstance(h):
            text = extractText(h)
            corpus = corpus + text
        else:
            corpus = corpus
    return corpus

def crawl(s):
    return text(s)
from bs4 import BeautifulSoup
import requests as r

def request(s):
    t = r.get(s)
    if t.status_code == 200:
        print(f"successfully requested {t}")
    else:
        print(f"error requesting {t}: {t.status_code}")
    return t.content

def crawl(s):
    html = BeautifulSoup(request(s))
    print(html.get_text())
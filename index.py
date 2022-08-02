import json
import chevron
import modules.crawl as crawl
import modules.analyze as analyze
import modules.generateHTML as generateHTML

def process(s, n, url):
    t = crawl.crawl(s)
    a = analyze.analyze(t, n, url)
    generateHTML.generateHTML(a)

f = open("sites.json", "r")

sites = json.loads(f.read())
print(sites)

for s in sites["sites"]:
    print(f"{s['sitename']}--{s['feedurl']}")
    process(s["feedurl"], s["sitename"], s["siteurl"])
    print(crawl.errorpages)

f.close()
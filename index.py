import json
import modules.crawl as crawl
import modules.analyze as analyze
import modules.generateHTML as generateHTML

def process(s):
    t = crawl.crawl(s)
    a = analyze.analyze(t)
    g = generateHTML.generateHTML(a)

sites = json.loads(open("sites.json"))
print(sites)

for s in sites:
    print(s.sitename)
    print(s.feedurl)
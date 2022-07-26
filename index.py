import json
import modules.crawl as crawl
# import modules.analyze as analyze
import modules.generateHTML as generateHTML

def process(s):
    t = crawl.crawl(s)
#    a = analyze.analyze(t)
    g = generateHTML.generateHTML(a)

f = open("sites.json", "r")

sites = json.loads(f.read())
print(sites)

for s in sites["sites"]:
    print(f"{s['sitename']}--{s['feedurl']}")
    crawl.crawl(s["feedurl"])

f.close()
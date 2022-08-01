import json
import modules.crawl as crawl
import modules.analyze as analyze
import modules.generateHTML as generateHTML

def process(s, n):
    t = crawl.crawl(s)
    a = analyze.analyze(t, n)
#     g = generateHTML.generateHTML(a)

f = open("sites.json", "r")

sites = json.loads(f.read())
print(sites)

for s in sites["sites"]:
    print(f"{s['sitename']}--{s['feedurl']}")
    process(s["feedurl"], s["sitename"])
    print(crawl.errorpages)

f.close()
import modules.crawl as crawl
import json

f = open("sites.json")
sites = json.loads(f.read())
print(sites)

cache = []

for s in sites["sites"]:
    site = {}
    corpus = crawl.HTMLcorpus(s)
    site["sitename"] = s["sitename"]
    site["content"] = corpus
    cache.append(site)
    print(crawl.errorpages)

f.close()

g = open("cache.json", "w")
g.write(cache)
g.close()
import modules.crawl as crawl
import json

f = open("sites.json", "r")

sites = json.loads(f.read())
print(sites)

cache = []

for s in sites["sites"]:
    print(f"{s['sitename']}--{s['feedurl']}")
    x = crawl.HTMLcorpus(s["feedurl"], True)
    cache.append(x)
    print(crawl.errorpages)

f.close()

print(cache)

g = open("cache.json", "w")
jsonreport = json.dumps(cache, indent=4)
g.write(jsonreport)
g.close()
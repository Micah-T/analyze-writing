# Analyze-writing
This project generates reading-ease reports on an entire website based off of an XML sitemap. It is run from `index.py`.

Currently this is hosted at [https://deploy.torcellini.org]. This is a Netlify site based off of a manually-generated Github repository, which is quite clumsy, but I had trouble getting the Python to work in Netlify. 

## Architecture

The sites themselves are stored in `sites.json`. `index.py` loops through them and passes the sitemaps through the `modules`.

## Caching
Run `cache.py` to create a `cache.json` for development purposes. 

## TODO
- Make it easier to use the `cache.json` file. 
- Add abilities to read other types of sitemaps and RSS/ATOM feeds. 
- Make this able to automatically deploy from Netlify. 
- Improve the content filtering algorithm in `crawl.py`.`ofSubstance()` to be a bit more versatile and accurate.  
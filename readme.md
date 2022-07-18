# Analyze-writing

It would be interesting to generate an analytical report from writing. To start, I would use a sitemap file from one of my websites (either an existing XML one* or create a JSON or CSV one**). With the former, I would have to construct a web spider and use natural language processing to analyze the vocabulary, which would give me flexibility to use it on websites that I do not control (I'm inclined towards this method). With the latter, I could customize the data file to make the Python coding somewhat easier. Once I had the data, the program would generate an HTML report which I could then host either as part of an existing website or at a torcellini.org subdomain. It would be easiest to host this as a static page, probably using Netlify. I would experiment different methods for automatic re-processing.

*for example, [htps://micah.torcellini.org/sitemap.xml] or [https://micah.torcellini.org/feed.xml].

** which I would generate using the same methods as the XML ones.

## Architecture


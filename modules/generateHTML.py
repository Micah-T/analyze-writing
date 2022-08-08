import chevron

def render(data):
    with open("templates/template.mustache", "r") as template:
        return chevron.render(template, data)

def slug(filename):
    return str(f"{filename.replace(' ', '-').replace( '.', '-')}.html".lower())

def write(content, filename):
    with open("_output/"+ slug(filename), "w") as f:
        f.write(content)   

def generateHTML(d):
    c = render(d)
    write(c, d["sitename"])

def writeIndex(pages):
    with open("templates/index.mustache") as template:
        html = chevron.render(template, pages)
    with open("_output/index.html", "w") as f:
        f.write(html)
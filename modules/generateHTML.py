import chevron

def render(data):
    with open("templates/template.mustache", "r") as template:
        return chevron.render(template, data)

def write(content, filename):
    with open(f"_output/{filename.replace(' ', '-').replace( '.', '-')}.html", "w") as f:
        f.write(content)   

def generateHTML(d):
    c = render(d)
    write(c, d["sitename"])
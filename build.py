import os
from jinja2 import Template

pages = []
blog = []

def read_files():
    for _, _, files in os.walk("./content"):
        for filename in files:
            title = filename.replace(".html", "")
            title = title.capitalize()
            pages.append({
                "filename": "./content/" + filename,
                "title": title,
                "output": "./docs/{}".format(filename)
            })
    for _, _, files in os.walk("./blog"):
        for filename in files:
            title = filename.replace(".html", "")
            title = title.capitalize()
            blog.append({
                "filename": "./blog/" + filename,
                "title": title,
                "output": "./docs/{}".format(filename)
            })


def gen_html():

    for p in pages:
        template = open("./templates/base.html").read()
        partial = open(p["filename"]).read()
        open(p["output"], "w+").write(template)


def gen_blog():

    for b in blog:
        template = open("./templates/blog.html").read()
        partial = open(b["filename"]).read()
        open(b["output"], "w+").write(template)


def fix_templates():

    for p in pages:
        partial = open(p["filename"]).read() 
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        template = template.render({'title': p['title'], 'content': partial})
        open(p["output"], "w+").write(template)

    for b in blog:
        partial = open(b["filename"]).read() 
        template_html = open("templates/blog.html").read()
        template = Template(template_html)
        template = template.render({'title': b['title'], 'blog': partial})
        open(b["output"], "w+").write(template)



def main():
    read_files()
    gen_html()
    gen_blog()
    fix_templates()
    print("Your files have been generated")

if __name__ == "__main__":
    main()

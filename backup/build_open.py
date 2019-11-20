import os
from jinja2 import Template

pages = []
blog = []

# blog =  [
#         {
#         "filename":"blog/blog1.html",
#         "date": "October 25th, 2019",
#         "title": "Kickstart Coding",
#         "output": "docs/blog1.html",
#         },
#         {
#         "filename":"blog/blog2.html",
#         "date": "October 30th, 2019",
#         "title": "Learning HTML",
#         "output": "docs/blog2.html",
#         },
#         {
#         "filename":"blog/blog3.html",
#         "date": "November 8th, 2019",
#         "title": "Learning CSS",
#         "output": "docs/blog3.html",
#         },
#         {
#         "filename":"blog/blog4.html",
#         "date": "November 11th, 2019",
#         "title": "Learning Python",
#         "output": "docs/blog4.html",
#         }
#         ]


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
    print(pages)
    print(blog)


def gen_html():

    for p in pages:
        template = open("./templates/base.html").read()
        partial = open(p["filename"]).read()
        template = template.replace("{{title}}", p["title"])
        template = template.replace("{{content}}", partial)
        open(p["output"], "w+").write(template)


def gen_blog():

    for p in blog:
        template = open("./templates/blog.html").read()
        partial = open(p["filename"]).read()
        template = template.replace("{{title}}", p["title"])
        template = template.replace("{{blog}}", partial)
        open(p["output"], "w+").write(template)

#Jinja stuff
def read_template():

    for file in pages:
        index_html = open(pages).read() 
        template_html = open("templates/base.html").read() 
        template = Template(template_html)
        template.render(title="Testpage",content=index_html)
        # Need to write output file 
        open(file["output"], 'w+').write(html_result)
        #print(template.render(title="Testpage",content=index_html))



def main():
    read_files()
    gen_html()
    gen_blog()
    #read_template()
    print("Your files have been generated")

if __name__ == "__main__":
    main()

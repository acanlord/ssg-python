#! /usr/bin/python

html_pages = [ 
    { 
        "filename": "./content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
    },
    {
        "filename": "./content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
    {

        "filename": "./content/blog.html",
        "output": "docs/blog.html",
        "title": "blog",
    }
]


blog_pages =  [
    {
    "filename":"blog/blog1.html",
    "date": "October 25th, 2019",
    "title": "Kickstart Coding",
    "output": "docs/blog1.html",
    },
    {
    "filename":"blog/blog2.html",
    "date": "October 30th, 2019",
    "title": "Learning HTML",
    "output": "docs/blog2.html",
    },
    {
    "filename":"blog/blog3.html",
    "date": "November 8th, 2019",
    "title": "Learning CSS",
    "output": "docs/blog3.html",
    },
    {
    "filename":"blog/blog4.html",
    "date": "November 11th, 2019",
    "title": "Learning Python",
    "output": "docs/blog4.html",
    }
    ]


# Helper Function
#get_file_contents takes in path to file & returns contents of file as stirng """
def get_file_contents(template):

    with open(template) as template_contents:
        return template_contents.read()

def gen_html(pages_list):
    """ Given a list of dictionary pages, iterates them and does stuff """


    for p in pages_list:
        with open(p["output"], 'w') as outfile:
                base_html = get_file_contents("templates/base.html")
                base_html = base_html.replace("{{title}}", p["title"])
                base_html = base_html.replace("{{content}}", get_file_contents(p["filename"]))
                outfile.write(base_html)

def gen_blog(blog_pages):

    for b in blog_pages:
        with open(b["output"], 'w') as outfile:
                base_blog = get_file_contents("templates/blog.html")
                base_blog = base_blog.replace("{{template}}", b["title"])
                base_blog = base_blog.replace("{{blog}}", get_file_contents(b["filename"])) 
                outfile.write(base_blog)

def main():
    gen_html(html_pages)
    gen_blog(blog_pages)
print("Done generating your files")

if __name__ == "__main__":
    main()

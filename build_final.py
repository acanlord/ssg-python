#! /usr/bin/python

import os

# Generate HTML content 







def get_file_contents(template):
    """ get_file_contents takes in path to file & returns contents of file as stirng """

    with open(template) as template_contents:
        return template_contents.read()




def gen_html(pages_list):
    """ Given a list of dictionary pages, iterates them and does stuff """

    base = "./templates/base.html"

    for p in pages_list:
        with open(p["output"], 'w') as outfile:
                base_html = get_file_contents(base)
                base_html = base_html.replace("{{title}}", p["title"])
                base_html = base_html.replace("{{content}}", get_file_contents(p["filename"]))
                outfile.write(base_html)

    return True


def main():
    """ entrypoint """

    my_pages = [ 
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

    if gen_html(my_pages):
        print('Done generating HTML files at docs/')
    else:
        print('oh shit')

if __name__ == "__main__":
    main()



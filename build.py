#! /usr/bin/python

# Generate HTML content 


pages = [ 
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





def get_template(template):
    with open(template) as template_contents:
        return template_contents.read()




def gen_html(pages):
    top = "./templates/top.html"
    bottom = "./templates/bottom.html"

    for p in pages:
        with open(p["output"], 'w') as outfile:

                # Get and dump 'top' template into 'output' file
                top_html = get_template(top)
                top_html = top_html.replace("{{title}}", p["title"])
                outfile.write(top_html)

                # Get and dump page.filename contents into page.output
                with open(p["filename"]) as infile:
                    outfile.write(infile.read())

                # Get and dump 'bottom' template into 'output' file
                outfile.write(get_template(bottom))
    
    return True


def main():
    if gen_html(pages):
        print('Done generating HTML files at docs/')
    else:
        print('oh shit')

if __name__ == "__main__":
    main()

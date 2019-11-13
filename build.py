pages = [
      {
          "filename": "content/index.html",
          "output": "docs/index.html",
          "title": "About Me",
      },
      {
          "filename": "content/projects.html",
          "output": "docs/projects.html",
          "title": "Projects",
      },
      {

          "filename": "content/blog.html",
          "output": "docs/blog.html",
          "title": "blog",
      }
      ]

blog =  [
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


def gen_html():

    for p in pages:
        base = "./templates/base.html"
        # Read in the entire template
        template = open(base).read()
        # Read in the content of the index HTML page
        index_content = open(p["filename"]).read()
        # Use the string replace
        template = template.replace("{{title}}", p["title"])
        finished_index_page = template.replace("{{content}}", index_content)
        open(p["output"], "w+").write(finished_index_page)


def gen_blog():

    for b in blog:
        blog_base = "./templates/blog.html"
        # Read in the entire template
        blog_template = open(blog_base).read()
        # Read in the content of the index HTML page
        blog_content = open(b["filename"]).read()
        # Use the string replace
        blog_template = blog_template.replace("{{title}}", b["title"])
        finished_blog_page = blog_template.replace("{{blog}}", blog_content)
        open(b["output"], "w+").write(finished_blog_page)

    return True


def main():
    gen_html()
    gen_blog()
    print("Your files have been generated")

if __name__ == "__main__":
    main()

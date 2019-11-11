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

    return True


def main():
    if gen_html():
        print('Done generating HTML files at docs/')
    else:
        print('oh snap, something went wrong')

if __name__ == "__main__":
    main()

from jinja2 import Template

def read_template():

    index_html = open("docs/index.html").read()
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    template.render(title="TestTest",content=index_html)

    read_template()
    print("udpate complete")

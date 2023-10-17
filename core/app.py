from jinja2 import Environment, FileSystemLoader
import os


def greet(persons):
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
    )
    template = env.get_template("greet_template.txt")
    return template.render(persons=persons)

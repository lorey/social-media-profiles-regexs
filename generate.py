from collections import OrderedDict
from json import JSONDecoder

from jinja2 import Template


def generate_readme():
    """
    This will create a README.md from the regexes.json and README.md.template file.
    """
    # render README to string
    readme_rendered = render_readme()

    # store it as README.md
    with open("README.md", "w") as output_file:
        output_file.write(readme_rendered)


def render_readme():
    with open("README.md.template") as template_file:
        template_content = template_file.read()

    with open("regexes.json") as data_file:
        # ensure json/dict order is consistent below python 3.6
        # -> testing for correct readme won't fail
        customdecoder = JSONDecoder(object_pairs_hook=OrderedDict)
        regexes = customdecoder.decode(data_file.read())

    template = Template(template_content)
    return template.render(data=regexes)


if __name__ == "__main__":
    generate_readme()
